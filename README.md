# Lab Experiments Repository

Organized lab experiments for 4 subjects - CS4501 Compiler Design, CS4V51 Cloud Computing, CS4503 Data Analytics and Visualization, and CS3691 Embedded Systems and IoT.

**Institution:** Chennai Institute of Technology, Chennai - 69

---

## Subject Folders

| Folder | Subject | Experiments |
|--------|---------|-------------|
| [COMPILER-DESIGN](./COMPILER-DESIGN/) | CS4501 Compiler Design | 10 |
| [CLOUD-COMPUTING](./CLOUD-COMPUTING/) | CS4V51 Cloud Computing | 9 |
| [DATA-ANALYTICS-AND-VISUALIZATION](./DATA-ANALYTICS-AND-VISUALIZATION/) | CS4503 Data Analytics | 5 (with sub-parts) |
| [EMBEDDED-PROGRAMMING](./EMBEDDED-PROGRAMMING/) | CS3691 Embedded Systems and IoT | 12 |

---

## Compiler Design Experiments

| No | Experiment | Files |
|----|-----------|-------|
| 01 | Symbol Table Implementation | `symbol_table.c` |
| 02 | Lexical Analyzer | `lexer.c` |
| 03 | Arithmetic Expression (LEX & YACC) | `art_expr.l`, `art_expr.y` |
| 04 | Valid Variable Recognition (LEX & YACC) | `valvar.l`, `valvar.y` |
| 05 | Control Structures Syntax (LEX & YACC) | `control.l`, `control.y` |
| 06 | Calculator (LEX & YACC) | `cal.l`, `cal.y` |
| 07 | Three Address Code Generation | `tac.l`, `tac.y` |
| 08 | Type Checking | `typecheck.c` |
| 09 | Code Optimization Techniques | `optimize.c` |
| 10 | Backend Compiler (TAC to 8086 Assembly) | `backend.c` |

## Cloud Computing Experiments

| No | Experiment | Files |
|----|-----------|-------|
| 01 | VirtualBox Installation | `README.md` |
| 02 | C Compiler in Virtual Machine | `hello.c`, `leapyear.c` |
| 03 | Google App Engine Hello World | `main.py`, `app.yaml` |
| 04 | GAE Launcher | `app.yaml`, `index.html` |
| 05 | CloudSim Simulation | `CloudSimExample.java` |
| 06 | File Transfer between VMs | `README.md` |
| 07 | Hadoop WordCount | `WordCount.java` |
| 08 | Docker First Container | `Dockerfile`, `main.py` |
| 09 | Docker Hub Container | `README.md` |

## Data Analytics Experiments

| No | Experiment | Files |
|----|-----------|-------|
| 01 | Installation and Exploration | `install_and_explore.py` |
| 02 | Data Handling (A-D) | `02a_numpy.py`, `02b_pandas.py`, `02c_reading.py`, `02d_iris.py` |
| 03 | Statistical Analysis - Diabetes (A-D) | `03a_univariate.py`, `03b_bivariate.py`, `03c_multiple.py`, `03d_comparison.py` |
| 04 | Visualization & Hypothesis Testing (A-D) | `04a_normal.py`, `04b_ztest.py`, `04c_ttest.py`, `04d_anova.py` |
| 05 | Model Building & Validation (A-C) | `05a_linear.py`, `05b_logistic.py`, `05c_timeseries.py` |

## Embedded Programming Experiments

| No | Experiment | Files |
|----|-----------|-------|
| 01 | 8051 Assembly - 8-bit Addition | `addition.asm` |
| 02 | Data Transfer - Registers & Memory | `type1.asm`, `type2.asm` |
| 03 | ALU Operations (8051 Assembly) | `alu_operations.asm` |
| 04 | Basic Programs (Embedded C) | `led_blink.c` |
| 05 | Arithmetic Programs (Embedded C) | `arithmetic.c` |
| 06 | Arduino Platform Programming (A-E) | `digital_write.ino`, `digital_read.ino`, `analog_read.ino`, `analog_write.ino`, `serial.ino` |
| 07 | IoT Communication - Bluetooth | `bluetooth_led_control.ino` |
| 08 | Raspberry Pi Python Programming | `led_blink.py`, `rgb_led.py`, `switch_led.py` |
| 09 | Interfacing Sensors (IR, Ultrasonic) | `ir_sensor.py`, `ultrasonic_sensor.py` |
| 10 | Arduino - Raspberry Pi Communication | `arduino_master.ino`, `raspberry_pi_slave.py` |
| 11 | Cloud Platform Data Logging (Blynk) | `log_data_to_blynk.py` |
| 12 | IoT Smart Home System | `smart_home_blynk.py` |

---

## How to Use

Each experiment folder contains:
- **Source code** file(s) ready to compile/run
- **README.md** with objective, setup, and run instructions

## Tools Required
- **Compiler Design**: GCC, LEX (Flex), YACC (Bison)
- **Cloud Computing**: VirtualBox, Google Cloud SDK, Docker, Eclipse (for CloudSim)
- **Data Analytics**: Python 3.x, pip packages: numpy pandas matplotlib seaborn scikit-learn statsmodels scipy
- **Embedded**: Keil uVision5, Arduino IDE 2.0, Thonny IDE (for Pico)
