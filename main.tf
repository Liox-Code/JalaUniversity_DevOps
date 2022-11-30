terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# Pulls the image
resource "docker_image" "nginx" {
  name = "nginx:latest"
}

# Create a container
resource "docker_container" "nginx_Terraform" {
  image = docker_image.nginx.image_id
  name  = "nginx_Terraform"

  ports {
    internal = 80
    external = 8080
  }

}
