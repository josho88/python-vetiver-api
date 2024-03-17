## ---------------------------
##
## Script name:
##
## Purpose of script: 
##
## Author: 
##
## Date Created: 
##
## Email: induco.sols@gmail.com
##
## ---------------------------
##
## Notes:


# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

## ---------------------------


library(shiny)
library(vetiver)
library(tidyverse)
library(httr)
library(flexdashboard)

baseURL <- 'http://127.0.0.1:8080' # <-- address our API is running, locally (in Docker) or remotely

# Define UI for application that draws a histogram
# Define UI for application that draws a histogram
ui <- fluidPage(
  
  # Application title
  titlePanel("MLOps Dashboard"),
  br(),
  # Sidebar with a slider input for number of bins 
  tagList(
    tabsetPanel(
      tabPanel(
        style = "padding:2%;",
        "Predict from your endpoint",
        br(),
        shiny::sliderInput('disp', 'Disp:', min = 0, max = 200, value = 30),
        br(),
        gaugeOutput("gauge", width = "300px")
      )
    )
  )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  pred <- reactive({
    req(input$disp)
    endpoint = vetiver_endpoint(paste(baseURL, 'predict', sep = '/'))
    new_car = tibble(disp = input$disp)
    pred = predict(endpoint, new_car)
    return(pred)
  })

  output$gauge <- renderGauge({
    gauge(pred()$predict, min = 20, max = 24, label = "MPG",
          gaugeSectors(success = c(24,23), warning = c(23,21), danger = c(21,20)))
  })
}

# Run the application 
shinyApp(ui = ui, server = server)