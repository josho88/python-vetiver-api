from vetiver import VetiverModel
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins

load_dotenv(find_dotenv())

b = pins.board_s3('airfinity-datascience-staging', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'vetiver-mpg-py', version = '20240306T180900Z-29d75')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app