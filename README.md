# Warstate Bot

A [pycord](https://pycord.dev/) based [discord](https://discord.com/) bot that uses the [unofficial helldivers 2 api](https://github.com/dealloc/helldivers2-api) to fetch and showcase current data about planets and major orders.

## Features

### Completed

- Major order: Using the `/orders` command, you are able to check the currently active major order.
- Planet Reports: Using the `/status` command, you are able to check the current liberations progress of a planet.
- Ping: Using the `/ping` command, you are able to see the current latency the bot is experiencing.

### Planned

- Campaign Reports: Using the `/active` command, you are able to see all current active campaigns and their data/progress.
- Scheduled Updates: Using the `/update` command, you are able to set a time and channel you'd like to receive automated Campaign Reports in.
- Set-up script: A bash script will be added to provide options for running the project.

## Requirements

I highly recommend you have [Docker](https://www.docker.com/products/docker-desktop/) installed for this bot.
Otherwise, please make sure you:
- Are on python 3.10 or higher

Also, make sure you have installed the following packages on their **latest release for your python version**:
- py-cord
- python-dotenv
- aiohttp
- datetime

You also need a valid source of an API, you can either do
- A: Use an existing source
    - Remove the `helldivers2` image from `docker-compose.yaml`
    - Update the `.env` accordingly (made in the steps below)
- B: Host your own source
    - You'll need [This api](https://github.com/dealloc/helldivers2-api) as a docker image called `helldivers2:latest`

I am aware of the inconvenience, and I'll work on providing a change for this soon.

## Installation

If using docker:
1. Clone the repo
2. Create a blank `.env` file in the project root.
3. Copy and paste the contents from `example.env` into `.env`
4. Launch the program using `docker-compose up --build -d`

## Usage

Once the bot is up and running, you can use the following commands to interact with it:

- `/status {name}` : To get the current status report of a planet.

![Orders command output](https://i.ibb.co/TL2FP1L/Screenshot-from-2024-03-07-01-36-37.png)

- `/orders` : To get the currently active major orders.

![Orders command output](https://i.ibb.co/6rJMfDF/Screenshot-from-2024-03-07-01-37-34.png)

- `/ping`  : See the current latency the bot is having.

![Ping command output](https://i.ibb.co/4Y2d6St/Screenshot-from-2024-03-07-16-22-36.png)

<!-- not ready yet
- `/active` : To gTo get a -ull-report of the currently active major orders aswell as status reportorform every planet currently marked with an offense or decence campaign.
- `/schedule` : To sTo set a channel and time you'd like the bot to sed a `/active` report to.
 -->

## Contributing

Contributions are welcome! If you'd like to contribute to warstate-bot, please follow these guidelines:

1. Fork the repository.
2. Switch to the `dev` branch: `git checkout dev`
3. Create a new branch from `dev`: `git checkout -b feature/your-feature-name`
4. Make your changes and commit them: `git commit -m 'Add some feature'`
5. Push to the `dev` branch: `git push origin feature/your-feature-name`
6. Submit a pull request.

## License

This project is licensed under the [BSD 2-Clause license](https://github.com/Jelle-Kuipers/Helldivers2-warstate-bot?tab=BSD-2-Clause-1-ov-file#).

## Contact

If you have any questions or suggestions regarding the bot, feel free to contact me at [jelle30kuipers@gmail.com](mailto:jelle30kuipers@gmail.com).

