# Water Vending Machine FSM

A simple Python program simulating a **Water Vending Machine** using a Finite State Machine (FSM) model.

---

## Overview

This program models the behavior of a water vending machine that accepts coins, dispenses water once sufficient funds are inserted, returns change if needed, and handles stock management. It includes an admin-only feature to refill water stock with password protection.

---

## Features

- **Finite State Machine implementation** with states:  
  - `Idle`  
  - `AcceptingCoins`  
  - `DispensingWater`  
  - `ReturningChange`
- Fixed water price (default: 40 cents) and initial stock (default: 10 portions)
- Accepts multiple coin insertions until the price is met or exceeded
- Dispenses water and returns change automatically
- Allows transaction cancellation with refund of inserted coins
- Admin authentication for stock refill
- Displays current machine status (state, balance, and stock)
- Graceful handling of out-of-stock and invalid inputs

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Program

1. Clone or download the repository.
2. Open a terminal/command prompt and navigate to the project folder.
3. Run the program