
class Config:
	# Proportion of tailgaters in the simulation (e.g. 0.1 means 10% tailgaters 90% normal drivers)
	PROPORTION = 0.4 # 0.0 0.4 0.1 1.0
	# Random seed
	SEED = 4

	START_VELOCITY = 50
	MIN_DISTANCE = 80
	MAX_SPEED = 75
	DECELERATION = 5
	EMERGENCY_DECELERATION = 7
	ACCELERATION = 6
	# Chance for random deceleration
	CHANCE = 0.56
	# We refer to a tailgater as TOKKIE in our code
	IS_TOKKIE = False
	TOKKIE_SPEED = 85
	TOKKIE_DISTANCE = 5

	REACTION_TIME = 1.8

	CAR_SIZE = 15
	CAR_HEIGHT = 4
	
	TICKSPEED = 0.5
	MAX_TICKS = 1000
	DATA_SIZE = 500

	SCREEN_WIDTH, SCREEN_HEIGHT = 2560, 800
	
	MAX_CARS = 250
	
	PLOT_FOLDER = "results"

