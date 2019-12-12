import argparse
from MarsRover.mars_rover import MarsRover

if __name__ == "__main__":

    print("=== Mars Rover Photo Downloader ===")

    parser = argparse.ArgumentParser(
        description='Mars rover photo downloader', add_help=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='?')
    parser.add_argument('--list-rovers', action='store_true', help="""
        List all available rovers.
    """)
    parser.add_argument('--list-cameras', action='store_true', help="""
        List all available cameras.
    """)
    parser.add_argument('--rover', 
        action="store", dest="rover", type=str, default="Curiosity", help="""
            Specify the motor vehicle on the surface of Mars.
    """)
    parser.add_argument('--sol', action="store", dest="sol", default=1, type=int, help="""
        Specify a martian day in which the photos were taken.
    """)
    parser.add_argument('--camera', action="store", dest="camera", default="FHAZ", type=str, help="""
        Specify the camera with which the photos were taken.
    """)
    parser.add_argument('--key', action="store", dest="key", type=str, help="""
        Specify your NASA public api key.
    """)

    parsed_args = parser.parse_args()
    print_list = lambda l: [print(x) for x in l]

    rover = parsed_args.rover
    sol = parsed_args.sol
    camera = parsed_args.camera,
    if type(camera) == tuple:
        camera = camera[0]
    api_key = parsed_args.key

    print(f"Selected rover: {rover}")
    print(f"Selected sol: {sol}")
    print(f"Selected camera: {camera}")
    print(f"Fetching data with the API Key: {api_key}")

    mars_rover = MarsRover(rover, sol, camera, api_key)

    if parsed_args.list_rovers:
        print_list(MarsRover.ROVER_LIST)
    elif parsed_args.list_cameras:
        print_list(MarsRover.CAMERA_LIST)

    print("Downloading photos...")

    mars_rover.save_links()

    print("Done!")
    print("Go to './MarsRover/out' to view the files.")