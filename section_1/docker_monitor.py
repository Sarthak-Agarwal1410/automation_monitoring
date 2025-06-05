import docker
import time
import logging
import sys

# Configuration
CPU_THRESHOLD = 80.0  # percentage
CHECK_INTERVAL = 5    # duration in seconds

# logging Setup
logging.basicConfig(
    filename='docker_monitor.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def get_cpu_percent(stats):
    try:
        cpu_delta = stats['cpu_stats']['cpu_usage']['total_usage'] - stats['precpu_stats']['cpu_usage']['total_usage']
        system_delta = stats['cpu_stats']['system_cpu_usage'] - stats['precpu_stats']['system_cpu_usage']
        if system_delta > 0 and cpu_delta > 0:
            cpu_count = len(stats['cpu_stats']['cpu_usage']['percpu_usage'])
            return (cpu_delta / system_delta) * cpu_count * 100.0
    except KeyError:
        logging.warning("Incomplete CPU stats found.")
    return 0.0

def monitor_containers(client):
    try:
        containers = client.containers.list()
        for container in containers:
            stats = container.stats(stream=False)
            cpu_percent = get_cpu_percent(stats)
            if cpu_percent > CPU_THRESHOLD:
                message = f"ALERT: Container '{container.name}' CPU usage is {cpu_percent:.2f}%"
                logging.warning(message)
                print(message)
            else:
                logging.info(f"Container '{container.name}' CPU usage: {cpu_percent:.2f}%")
    except docker.errors.APIError as e:
        logging.error(f"Docker API Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

def main():
    try:
        client = docker.from_env()
        print("Monitoring Docker containers. Press Ctrl+C to stop.")
        while True:
            monitor_containers(client)
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("Stopping monitor...")
        logging.info("Monitoring stopped by user.")
    except docker.errors.DockerException as e:
        logging.critical(f"Failed to connect to Docker: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
