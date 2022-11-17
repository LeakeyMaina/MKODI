# Azure App Service is a PaaS service able to run Docker containers, that suits best for this scenario. 
# Azure Container Registry holds the Docker images ready to be pulled from the App Service. 
# An Azure KeyVault instance can store application secrets such as connection strings.
# Database server—Azure Database for Postgresql 
# Service Bus to allow asynchronous communication between the services.
terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.31.0"
    }
  }
}

provider "azurerm" {
  subscription_id = "17a163e1-cd14-4a6a-80c4-05945f55fa55"
  client_id       = "bef8bc2e-ee98-4fee-95d1-736c7a549f7b"
  client_secret   = "lMI8Q~oFvaJXlGbG4AGrlT61XjQKdqFMqo1HKbeC"
  tenant_id       = "e50252cb-70fc-4a19-9c59-0cf02c9bf284"
  features {}
}


locals {
  resource_group="app-grp"
  location="North Europe"
}


resource "azurerm_resource_group" "app_grp"{
  name=local.resource_group
  location=local.location
}
resource "azurerm_service_plan" "mkodi-service-plan" {
  name                = "mkodi-service-plan"
  location            = azurerm_resource_group.app_grp.location
  resource_group_name = azurerm_resource_group.app_grp.name
  os_type             = "Windows"
  sku_name            = "B1"
}

resource "azurerm_windows_web_app" "mkodi" {
  name                = "mkodi"
  resource_group_name = azurerm_resource_group.app_grp.name
  location            = azurerm_resource_group.app_grp.location
  service_plan_id     = azurerm_service_plan.mkodi-service-plan.id

  site_config {}
}