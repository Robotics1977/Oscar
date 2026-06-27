# 🤖 Oscar — Autonomous Outdoor Utility Rover
**Platform:** Raspberry Pi 5 (8GB) + Wheelchair Motors  
**Role:** Outdoor autonomous utility vehicle (mowing, plowing, towing, augering, and more)  
**OS / Stack:** Ubuntu + ROS 2 Jazzy  
**Communication:** ROS 2 + MQTT for sensor/NOVAGrid integration  
**Status:** Planned / Parts Acquisition Phase

---

## 📘 Overview
Oscar is NOVAGrid's heavy-duty outdoor rover, built as a multifunctional utility platform rather than a single-purpose mower. The autonomous drivetrain base is being built first; attachments (mowing deck, snow plow, post auger, cart) are added afterward.

The concept merges:
- Two repurposed 24V wheelchair motors (differential drive — drive and steering combined)
- A Raspberry Pi 5 (8GB) compute unit
- A donor riding lawnmower frame and components
- Front-end omni or fabricated swivel wheels
- Long-range WiFi back to NOVAGrid

Oscar represents the outdoor robotics branch of NOVAGrid. Theme: painted green with a "Oscar the Grouch" trash can aesthetic.

---

## 🔩 Hardware

### Drivetrain (confirmed)
| Component | Notes |
|---|---|
| **2x Wheelchair motors** | 24V, unknown RPM/torque specs, sourced from eBay. Pending spin test. |
| **2x IBT-2 motor drivers** | One per drive motor, rated up to 43A — required, TB6612FNG on hand is insufficient (1.2A) |
| **3rd IBT-2 driver** | Needed for mowing deck motor — may need to order one more |
| **Front wheels** | Passive — needs swivel capability (caster or fabricated swivel mount) since fixed wheels would bind against differential-drive steering. Have wheels, round bar, pillow blocks on hand; swivel mount still needs fabrication. |
| **24V brakes** | Both wheelchair motors have integrated 24V brakes — must be powered to release |

### Compute / Brain (confirmed)
| Component | Notes |
|---|---|
| **Raspberry Pi 5 (8GB)** | Chosen for driver maturity/reliability after Orange Pi 4 Pro proved unusable (WiFi RX driver failure on early A733 chipset — board repurposed as wired Reolink client instead) |
| **SSD: Samsung EVO 128GB (used)** | Via SATA-to-USB adapter (5Gbps sufficient, SATA III is the limiting factor) |
| **Microcontroller: Arduino Nano** | Handles IBT-2 PWM control + 433MHz E-stop watchdog, independent of Pi |

### Sensors (confirmed additions)
| Component | Notes |
|---|---|
| **RPLIDAR S2 (IP65)** | Outdoor-rated — standard A1M8 (used on Alfred 1) and standard S2 not sunlight/weather rated |
| **Arducam 1080P IMX291 (waterproof metal case)** | USB/UVC camera, native Ubuntu support, low-light capable |
| **BNO055** | 9-DOF IMU w/ sensor fusion — chosen over MPU-6050/9250 for better outdoor heading accuracy |
| **INA260** | Battery voltage/current monitoring (already proven on solar project) |

### Power (confirmed)
| Component | Notes |
|---|---|
| **2x 12V 20Ah LiFePO4 (series = 24V 20Ah / ~480Wh)** | Easier to source than single 24V pack; outlasts Ryobi 40V 8Ah (320Wh) baseline with margin |

### Donor / Repurposed Hardware
| Source | Use |
|---|---|
| **Riding lawnmower** | Frame, wheels, axles — deck motor likely too large, will be evaluated separately |
| **Electric wheelchair (single drive motor)** | Candidate for mowing deck spindle motor — 24V native, no separate voltage needed |
| **Existing tow-behind cart** | Already owned, attaches via hitch |
| **Post auger** | Already owned, candidate future attachment |

### Custom Electronics
| Item | Notes |
|---|---|
| **IBT-2 distribution PCB** | Breakout/power-rail board for 3x IBT-2 + Nano (shared 5V/GND rails, signal headers) — smaller/cheaper than Alfred 1's PCB since IBT-2s are standalone boards, not integrated |

---

## 🧠 Software Architecture
- GPS + odometry fusion (GPS module not yet selected)
- Outdoor SLAM (cartographer or similar)
- Perimeter mapping
- Mowing/work patterns
- Safety interlocks (433MHz E-stop via Nano, independent of Pi)
- Remote kill-switch

---

## 🔮 Planned Features / Attachments
- Mowing deck (electric preferred, gas acceptable if donated mower available)
- Snow plow attachment — **likely first deployment**, avoids competing with mowing season timeline
- Post auger attachment
- Tow cart (already owned)
- Docking/charging station (inspired by Frengen Engineering's mower garage concept) — auto-return and charge
- Teleoperation mode as fallback/manual override

---

## 💰 Cost Lessons Learned
- Orange Pi 4 Pro + 128GB NVMe + 2230→2280 adapter bracket = sunk cost; board repurposed as wired Reolink camera client (ethernet confirmed solid, WiFi RX is fundamentally broken on current driver/image — board is too new, mainline Linux support still in progress as of mid-2026)
- Pi 5 8GB chosen deliberately over 4GB despite cost gap — autonomy safety case justifies the spend
- Pi 5 purchase **deferred** — using a spare SSD swapped into the existing Alfred 1 Pi 5 for early Oscar testing/dev without buying second hardware yet
- RPLIDAR S2 IP65 (~$330) is the next big remaining expense and is gating final brain purchase

---

## 🗓 Development Roadmap
1. ~~Spin-test wheelchair motors~~ (in progress)
2. Acquire remaining core components: batteries, RPLIDAR S2 IP65 — in progress
3. Design/fabricate front swivel mounts
4. Design IBT-2 distribution PCB
5. Build autonomous base (drivetrain + brain + core sensors) — no mowing deck yet
6. Get base driving/navigating reliably
7. Add first attachment — **snow plow** (off-season from mowing, avoids timeline conflict)
8. Add mowing deck for next mowing season
9. Future: docking/charging station, post auger, additional attachments

**Timeline:** No hard deadline. Preferred working seasons: Fall and Spring (avoiding Kansas summer heat and winter cold for build/test work).
