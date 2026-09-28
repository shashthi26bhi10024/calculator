# 1. Project Overview

 Calculator is a modular Python calculator project developed for the VITyarthi Build Your Own Project assignment. It is designed to demonstrate problem solving, functions, modular programming, input validation, error handling, and a clear software workflow.

The project is organized into five functional modules:

1. Basic Calculator
2. Advanced Calculator
3. Calculation History
4. Memory Functions

A Tkinter-based graphical interface is planned as the main user interface.

## 2. Features

### Basic Calculator
- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero error handling

### Advanced Calculator
- Percentage
- Square
- Square root
- Power
- Invalid-input handling

### Calculation History
- Store calculations during the current session
- Display calculation history
- Clear calculation history

### Memory Functions
- M+ — add a value to memory
- M− — subtract a value from memory
- MR — recall memory
- MC — clear memory

## 3. Technologies Used

- Python 3
- Tkinter for the graphical user interface
- Python `math` module for scientific calculations
- VS Code for development
- Git/GitHub for version control

## 4. Project Structure

```text
calculator/
├── main.py
├── basic.py
├── advanced.py
├── history.py
└── memory.py

## 5. Installation and Running

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal in the project folder.
4. Run

## 6. Testing

The individual modules should be tested with valid and invalid inputs.

Examples:
- `10 + 5` → `15`
- `10 ÷ 0` → division-by-zero error
- `√25` → `5`
- `√-4` → square-root error
- `sin(30°)` → approximately `0.5`
- `log(100)` → `2`
- Empty history → `No calculations yet.`
- Memory sequence `M+ 50`, `M+ 20`, `M− 10` → memory value `60`

## 7. Non-Functional Requirements

- Usability: The calculator should have a simple and understandable interface.
- Reliability:Invalid mathematical operations should be handled without crashing the application.
- **Maintainability:- Each major function group is separated into its own Python module.
- performance: Calculations should be performed quickly for normal user inputs.
- Error Handling: Invalid operations such as division by zero and invalid logarithm/square-root inputs should produce clear errors.

## 8. Future Enhancements

- Complete and improve the Tkinter graphical interface
- Add keyboard input
- Add more scientific functions
- Add persistent history using a file or database
- Add themes and improved user interface design
- Add automated unit tests

## 10. Author
Shashthi Chawla


