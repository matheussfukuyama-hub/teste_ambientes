# GitHub Workflow Test Project

This project is designed to demonstrate a GitHub workflow for development, staging, and production environments. It includes a simple application structure with GitHub Actions workflows for each environment.

## Project Structure

```
github-workflow-test
├── src
│   └── index.js
├── .github
│   └── workflows
│       ├── dev.yml
│       ├── staging.yml
│       └── production.yml
├── package.json
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/github-workflow-test.git
   ```

2. Navigate to the project directory:
   ```
   cd github-workflow-test
   ```

3. Install the dependencies:
   ```
   npm install
   ```

## Usage

To run the application, execute the following command:
```
node src/index.js
```

## GitHub Workflows

- **Development Workflow**: Defined in `.github/workflows/dev.yml`, this workflow runs on every push to the development branch.
  
- **Staging Workflow**: Defined in `.github/workflows/staging.yml`, this workflow is triggered after pull requests are merged into the main branch, deploying the application to the staging environment.

- **Production Workflow**: Defined in `.github/workflows/production.yml`, this workflow is executed after staging tests are approved, deploying the application to the production environment.

## Contributing

Feel free to submit issues or pull requests to improve this project.