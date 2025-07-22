# l10n_py2

⚠️ **This module is currently under active development and is not yet ready for production use.**
Features are being implemented incrementally, and many key components are still missing or incomplete.

---

Accounting localization module for **Paraguay**, developed entirely from scratch for Odoo 18.0. The goal is to provide a scalable, clean and complete localization package that complies with Paraguayan tax and accounting regulations.

## Current Status

So far, it includes:

- Initial model structure
- Departments of Paraguay loaded as states
- Basic fiscal responsibility types
- Chart of Accounts (in proccess)

Planned features (not implemented yet):
- Full chart of accounts
- Electronic invoicing validation
- Local journal configuration rules
- Reports and tax documents according to Paraguayan law

## Requirements

- Odoo 18.0 (development branch)
- Core Odoo modules: `account`, `base`, `contacts`, `latam_base`

## Installation

1. Clone this repository into your custom addons folder:
   ```bash
   git clone https://github.com/your_username/l10n_py2.git
