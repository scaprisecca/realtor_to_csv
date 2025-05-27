# Property Scraper Docker

This is a dockerized version of the property scraper script.

## Usage

```bash
docker-compose up --build

This will build the image and run the container.

The scraped listings will be saved in the `scraped_listings` directory.

```bash
docker-compose down
```

This will stop and remove the container.

```bash
docker-compose down --volumes
```

This will stop and remove the container and remove the volumes.

```bash
docker-compose down --volumes --remove-orphans
```

This will stop and remove the container and remove the volumes and remove any orphaned containers.

```bash
docker-compose down --volumes --remove-orphans --rmi all
```

This will stop and remove the container and remove the volumes and remove any orphaned containers and remove all images.

