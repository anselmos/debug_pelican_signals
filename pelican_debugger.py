from pelican import parse_arguments
from pelican import get_instance

pelican, settings = get_instance(parse_arguments())
pelican.run()
