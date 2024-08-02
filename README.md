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

Run the application:

```sh
python main.py
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
