# Migration Script Generator

This script provides an automated way to generate migration versions using Alembic.

## Dependencies

- `fabric`

## Usage

Go to the directory dev-utils:
```bash
cd dev-utils
```
from root of the repository.

The primary function provided by this script is `generate_version`.

### `generate-version`

Generates a new migration version.

#### Parameters:

- `c`: The context object (provided by Fabric).
- `message`: A string that represents the migration version name. Defaults to an empty string.

#### Example:

```bash
cd dev-utils
fab generate-version --message="Your migration version name here"
```

#### How it works:

1. The script uses Alembic to generate a new revision with a revision ID based on the current date and time.
2. It then creates a new directory for the migration, using the revision ID and provided message.
3. Inside this directory, two files are created: UP.sql and DOWN.sql.