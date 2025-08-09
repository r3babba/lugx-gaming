# LUGX Gaming

LUGX Gaming is an online gaming shop based on the design from [TemplateMo](https://templatemo.com/tm-589-lugx-gaming). This project implements the frontend and a backend API to analyze website data and present it on a visualization dashboard.

## 🚀 Overview

This project is a microservices-based application for an online gaming store. It includes a frontend for the user interface, a service to manage games, and a service to handle orders.

## ✨ Features

*   **Frontend:** A responsive and visually appealing user interface for browsing and purchasing games.
*   **Game Service:** Manages the game catalog, including adding, updating, and retrieving game information.
*   **Order Service:** Handles the purchasing process, including creating and managing orders.
*   **Analytics Dashboard:** Visualizes website data to provide insights into user behavior and sales trends.

## 🏛️ Architecture

The application is built using a microservices architecture, with separate services for the frontend, games, and orders. This design allows for independent development, deployment, and scaling of each service.

*   **Frontend:** The frontend is a static website built with HTML, CSS, and JavaScript. It is served by a containerized web server.
*   **Game Service:** A Python Flask application that provides a RESTful API for managing games.
*   **Order Service:** A Python Flask application that provides a RESTful API for managing orders.

## 🏁 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   [Docker](https://www.docker.com/get-started)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1.  Clone the repo
    ```sh
    git clone https://github.com/r3babba/lugx-gaming.git
    ```
2.  Navigate to the project directory
    ```sh
    cd lugx-gaming
    ```
3.  Build and run the services using Docker Compose
    ```sh
    docker-compose up --build
    ```

## 🎮 Usage

Once the services are running, you can access the application in your web browser:

*   **Frontend:** [http://localhost:8080](http://localhost:8080)
*   **Game Service API:** [http://localhost:5001](http://localhost:5001)
*   **Order Service API:** [http://localhost:5002](http://localhost:5002)

## 🛠️ Services

### Frontend

The frontend is located in the `lugx_frontend` directory. It contains the HTML, CSS, and JavaScript files for the user interface.

### Game Service

The game service is located in the `game-service` directory. It is a Python Flask application that manages the game catalog.

### Order Service

The order service is located in the `order-service` directory. It is a Python Flask application that handles the purchasing process.

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.