# Kubewizard

**Kubewizard** is An AI-Agent for automated Kubernetes troubleshooting, deployment, and management, based on LangChain and k8s related tools.

[![asciicast](https://asciinema.org/a/XS80PxLxtmurqMw6LU7UJtzhb.svg)](https://asciinema.org/a/XS80PxLxtmurqMw6LU7UJtzhb)

## Features

- Troubleshoot Kubernetes issues automatically
- Manage Kubernetes resources
- Search latest Kubernetes knowledge from internet
- Human in the Agent Loop, need approve when dangerous commands
- Chat memory
- Interactive console

## Usage

Run the application with interactive console:

Add your env variables in `.env` file:
```sh
OPENAI_API_KEY=your_openai_api_key
KUBECONFIG=your_kubeconfig_path
```

```sh
python main.py
```

Commands:
```sh
kubewizard>: help
Available commands:
  - clear  :  Clear the chat history.
  - history:  Display the chat history.
  - help   :  Print help info.
  - exit   :  Exit the application.
  - *      :  Ask me everything about your kubernetes cluster(why my nginx pod not ready)
```

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/kubewizard.git
   cd kubewizard
   ```

2. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Copy the example environment file and configure it, set your `OPENAI_API_KEY` and `KUBECONFIG`
   ```sh
   cp .env.example .env
   ```

## License

This project is licensed under the terms of the Apache-2.0 license. See the [`LICENSE`](./LICENSE) file for details.
