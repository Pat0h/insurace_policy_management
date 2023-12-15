# Insurance System

This Python-based Insurance System is a command-line application designed to manage policies, policyholders, and claims within an insurance company. It utilizes SQLAlchemy for database management and Click library to create a user-friendly command-line interface.

## Features

- **Policy Management**: Create, retrieve, update, and delete insurance policies.
- **Policyholder Management**: Manage policyholders, including creation, retrieval, and deletion.
- **Claim Handling**: Register and manage claims associated with policies.
- **Premium Calculation**: Calculate insurance premiums based on policy type, coverage, and policyholder age.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/insurance-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd insurance-system
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Ensure you have a Python environment set up. Then, you can interact with the insurance system through the command-line interface.

### Initialization

Before using the system, initialize the database:

```bash
python create.py
```

### Command-Line Interface

Use the CLI commands to interact with the system:

- **Create Policyholder**:
  ```bash
  python cli.py create-policyholder --name "John Doe" --email "john@example.com" --phone-number "1234567890" --address "123 Main St"
  ```

- **Create Policy**:
  ```bash
  python cli.py create-policy --policyholder-id 1 --start "2023-01-01" --end "2024-01-01" --coverage "comprehensive"
  ```

- **Create Claim**:
  ```bash
  python cli.py create-claim --policy-id 1 --claim-date "2023-06-15" --claim-details "Car accident" --status "Pending"
  ```

- **Get Policy**:
  ```bash
  python cli.py get-policy 1
  ```

- **Get Policyholder**:
  ```bash
  python cli.py get-policyholder 1
  ```

- **Remove Policy**:
  ```bash
  python cli.py remove-policy 1
  ```

- **Remove Policyholder**:
  ```bash
  python cli.py remove-policyholder 1
  ```

- **Remove Claim**:
  ```bash
  python cli.py remove-claim 1
  ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for new features, improvements, or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
