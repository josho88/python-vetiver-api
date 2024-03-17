from vetiver.data import mtcars
from sklearn.linear_model import LinearRegression
from vetiver import VetiverModel, vetiver_pin_write
import os
import pins

car_mod = LinearRegression().fit(mtcars.drop(columns="mpg"), mtcars["mpg"])

# create as a vetiver model
v = VetiverModel(car_mod, model_name = "vetiver-mpg-py", 
                 prototype_data = mtcars.drop(columns="mpg"))
v.description

# connect to s3 board
board = pins.board_s3("airfinity-datascience-staging", allow_pickle_read = True)

# write (or 'pin') the vetiver model to the s3 board
vetiver_pin_write(board, v)

