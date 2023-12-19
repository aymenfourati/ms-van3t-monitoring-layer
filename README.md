
## Mini-project: Simulation of the Internet of Vehicles (IoV): ms-van3t

#### Supervised by : Dr AFIF Meriem
#### Elaborated by : Fourati Aymen & Helali Eya

#### Academic year : 2023-2024

---------------------------------------------------------------------------


### Plan 

Introduction
Theoretical study
802.11p (ITS-G5) 
LTE-V2X (Long-Term Evolution Vehicle-to-Everything) 
NR-V2X (New Radio Vehicle-to-Everything) 
Introduction to ms-van3t
Introduction
Dependencies
Experimentation
Simulation : V2V example and V2V applications
Simulation : V2X emulator application
Interpreting results
Areas of improvement
Conclusion
Webography


---------------------------------------------------------------------------
### Introduction 

We propose to carry out a simulation of the Internet of Vehicles (IoV): ms-van3t : The project objective is to simulate 3 different use cases, namely 802.11p, lte-v2x and nr-v2x, in order to compare the differences between these 3 types of architectures and determine their different performances and limitations.

---------------------------------------------------------------------------
### Theoretical study

From Wikipedia, the free encyclopaedia

The IEEE 802.11p amendment adds Wireless Access in Vehicular Environments (WAVE) for vehicle communication systems.

It enhances the 802.11 (Wi-Fi) standard to support intelligent transportation system (ITS) applications in vehicles.

It enables data exchange between high-speed vehicles and between vehicles and road infrastructure (V2X) in the 5.9 GHz ITS band, with IEEE 1609 as the top-layer standard and ETSI ITS-G5 as the associated European standard.

802.11p (ITS-G5) :

A wireless communication standard specifically designed for road safety applications.

Mainly used for vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communication in intelligent transportation systems (ITS).

Advantages: Low latency, dedicated safety communication, ideal for safety alerts and real-time traffic information.

Limitations: Limited range, limited bandwidth, primarily focused on safety rather than entertainment or navigation services.


From Wikipedia, the free encyclopaedia

Cellular V2X (C-V2X) is a communications standard for V2X applications, including autonomous cars, developed by 3GPP as an alternative to IEEE 802.11p.


C-V2X uses 3GPP-standardised 4G LTE or 5G cellular connectivity to enable message exchanges between vehicles, pedestrians and roadside traffic control devices.


It typically uses the 5.9 GHz frequency band, officially designated for Intelligent Transport Systems (ITS), and offers around 25% greater range than DSRC (Dedicated Short Range Communications).

LTE-V2X (Long-Term Evolution Vehicle-to-Everything) :

Uses existing LTE networks to support vehicle-to-everything (V2X) communication, including V2V, V2I, V2P (vehicle-to-pedestrian) and V2N (vehicle-to-network).

Offers wider connectivity and higher bandwidth than 802.11p.


Advantages: High-speed connection, flexibility to support various IoV applications, scalability.

Limitations: Dependence on existing cellular infrastructure, risk of latency due to network congestion.


NR-V2X (New Radio Vehicle-to-Everything) :

Based on the 5G New Radio (NR) standard and designed for V2X communication.
Offers improved performance over LTE-V2X in terms of data rate and latency.

Advantages: High throughput, low latency, support for a variety of applications, including entertainment and navigation services.

Limitations: Requires 5G infrastructure, potentially higher cost.

---------------------------------------------------------------------------
### Introduction to ms-van3t
Introduction

ns-3 modules to build and simulate ETSI-compliant VANET (V2X) applications using SUMO (v-1.6.0+) and ns-3 (ns-3-dev, version supporting the NR-V2X module by CTTC), with the possibility of easily switching stack and communication technology.

Dependencies 

SUMO : "Simulation of Urban MObility" is an open source, highly portable, microscopic and continuous traffic simulation package designed to handle large networks. It allows for intermodal simulation including pedestrians and comes with a large set of tools for scenario creation.


Install SUMO : 

sudo add-apt-repository ppa:sumo/stable
sudo apt update
sudo apt install sumo sumo-tools sumo-doc


Close the github repo : 

git clone https://github.com/marcomali/ms-van3t



Run, from this repository :

./sandbox_builder.sh install-dependencies



Configure ns3 :

./ns3 configure --build-profile=optimized --enable-examples --enable-tests --disable-python --disable-werror


Build ns3 : 

./ns3 build

---------------------------------------------------------------------------

### Experimentation
Simulation : Sample V2V example and V2V applications

The project, Simulation de l’internet des véhicules (IoV): ms-van3t, focuses on running simulations of three vehicle-to-vehicle (V2V) communication technologies: 802.11p, LTE-V2X Mode 4 (CV2X), and NR-V2X Mode 2 (NRV2X). The simulations involve the creation of nodes in the ns3 simulation as vehicles enter the SUMO simulation, each implementing a full V2X stack at lower layers.

ms-van3t currently supports three stacks/communication technologies for V2V:

802.11p (sample program name: v2v-emergencyVehicleAlert-80211p)
LTE-V2X Mode 4 (sample program name: v2v-emergencyVehicleAlert-cv2x)
NR-V2X Mode 2 (sample program name: v2v-emergencyVehicleAlert-nrv2x))


To run the program:

./ns3 run "v2v-emergencyVehicleAlert-cv2x"
./ns3 run "v2v-emergencyVehicleAlert-80211p"
./ns3 run "v2v-emergencyVehicleAlert-nrv2x"


The SUMO scenario consists of a ring-like topology with two directions and two lanes for each direction (totaling 4 lanes).
Code Structure:

CAMs and DENMs dissemination logic is housed in modules within the automotive/Facilities folder.
Application logic is contained in emergencyVehicleAlert.cc/.h within the automotive/Applications folder.
Users are advised not to modify code in "Facilities," "BTP," or "GeoNet" folders, but to use ETSI Facilities Layer methods within the application.


CAM : Cooperative Awareness Message
DENM : Decentralized Environmental Notification Message
ETSI : European Telecommunications Standards Institute

Every vehicle that enters the scenario will start sending CAMs with a frequency between 1 Hz and 10 Hz (according to the ETSI standards). 

The vehicles are divided into "passenger" vehicles (i.e., normal vehicles) and "emergency" vehicles.

Nodes are created in the ns3 simulation as vehicle enters the SUMO simulation
A full NR-V2X, LTE-V2X or 802.11p stack is implemented at lower layers


A CAM generated by an emergency vehicle will have the "StationType" Data Element (i.e. a field of the message) set to "specialVehicles".

When normal vehicles receive these CAM messages from an emergency vehicle, they will check whether their heading is similar to the one of the emergency vehicle and which is their distance to the latter.

-> If the heading is similar and the distance is small enough, it means that the emergency vehicle is approaching. In this case, the receiving vehicles will either slow down (if on a different lane than the one the emergency vehicle is traveling on) or change lane as soon as possible (speeding up for a little while, if necessary, when they are on the same lane as the emergency vehicle).

When acting, in the SUMO GUI, vehicles will either turn orange (different lane --> slow down) or green (same lane --> clear path as soon as possible).

The SUMO scenario comprehends a ring-like topology, with two directions and two lanes for each direction (with a total of 4 lanes).



Setting up the environment :

<!-- number of vehicles:20 -->
<!-- generated on 2023-11-18 16:49:03.286463 by "cars.rou.xml -m 1 -r 1.4 -t 20" -->
<routes>
  <route id="0" edges="ne_to_nw nw_to_sw sw_to_se se_to_ne"/>
  <route id="1" edges="se_to_sw sw_to_nw nw_to_ne ne_to_se"/>
  <route id="2" edges="nw_to_sw sw_to_se se_to_ne ne_to_nw"/>
  <route id="3" edges="sw_to_nw nw_to_ne ne_to_se se_to_sw"/>
  <route id="4" edges="sw_to_se se_to_ne ne_to_nw nw_to_sw"/>
  <route id="5" edges="nw_to_ne ne_to_se se_to_sw sw_to_nw"/>

  <vType accel="4" decel="7.5" emergencyDecel="10" minGap="1.0" id="Car0" vClass="emergency"  maxSpeed="20.83"/>
  <vType accel="4" decel="7.5" emergencyDecel="10" minGap="1.0" id="Car1" maxSpeed="5.55"/>
  <vType accel="4" decel="7.5" emergencyDecel="7" minGap="1.0" id="Car2" maxSpeed="6.94"/>
  <vType accel="4" decel="7.5" emergencyDecel="10" minGap="1.0" id="Car3" maxSpeed="8.33"/>
  <vType accel="4" decel="7.5" emergencyDecel="10" minGap="1.0" id="Car4" maxSpeed="9.72"/>
  <vType accel="4" decel="7.5" emergencyDecel="10" minGap="1.0" id="Car5" maxSpeed="11.11"/>
  <vType accel="4" decel="7.5" emergencyDecel="10" minGap="1.0" id="Car6" maxSpeed="12.5"/>
  <vType accel="4" decel="7.5" emergencyDecel="10" minGap="1.0" id="Car7" maxSpeed="13.89"/>
  <vType accel="4" decel="7.5" emergencyDecel="10" minGap="1.0" id="Car8" maxSpeed="15.27"/>
  <vType accel="4" decel="7.5" emergencyDecel="10" minGap="1.0" id="Car9" maxSpeed="16.66"/>

      <vehicle id="veh1" type="Car2" depart="0.305337402498" route="0">
    </vehicle>
      <vehicle id="veh2" type="Car0" depart="0.600133874271" route="0">
    </vehicle>
      <vehicle id="veh3" type="Car2" depart="4.64994493787" route="1">
    </vehicle>
      <vehicle id="veh4" type="Car0" depart="4.76851800147" route="5">
    </vehicle>
      <vehicle id="veh5" type="Car5" depart="5.27469051452" route="3">
    </vehicle>
      <vehicle id="veh6" type="Car3" depart="5.37358402415" route="2">
    </vehicle>
      <vehicle id="veh7" type="Car5" depart="5.37486517084" route="2">
    </vehicle>
      <vehicle id="veh8" type="Car9" depart="5.47199197979" route="0">
    </vehicle>
      <vehicle id="veh9" type="Car2" depart="7.3802238939" route="3">
    </vehicle>
      <vehicle id="veh10" type="Car2" depart="7.48089324934" route="3">
    </vehicle>
      <vehicle id="veh11" type="Car4" depart="8.52374230514" route="4">
    </vehicle>
      <vehicle id="veh12" type="Car2" depart="8.68039033045" route="4">
    </vehicle>
      <vehicle id="veh13" type="Car8" depart="8.7260736113" route="0">
    </vehicle>
      <vehicle id="veh14" type="Car5" depart="9.87668718891" route="5">
    </vehicle>
      <vehicle id="veh15" type="Car7" depart="10.3751059437" route="4">
    </vehicle>
     <vehicle id="veh16" type="Car9" depart="12.0392872197" route="0">
    </vehicle>
      <vehicle id="veh17" type="Car5" depart="12.0993573071" route="2">
    </vehicle>
      <vehicle id="veh18" type="Car7" depart="12.6368142357" route="5">
    </vehicle>
      <vehicle id="veh19" type="Car2" depart="14.1847255129" route="1">
    </vehicle>
      <vehicle id="veh20" type="Car2" depart="15.9241824341" route="0">
    </vehicle>
</routes>

At a glance, in 802.11p vehicles broadcast periodic CAM messages and an RSU periodically broadcasts DENM messages to inform vehicles traveling in a low speed area to slow down. In this case CAMs and DENMs messages are encapsulated inside BTP and GeoNetworking. In LTE, instead, the CAM messages are forwarded to a remote host (behind an eNB + EPC), which analyzes the position of the vehicles and sends unicast DENMs to vehicles entering a low speed area to change their maximum allowed speed.
---------------------------------------------------------------------------
### Simulation : Sample V2X emulator application

The ms-van3t project also includes a V2X emulator application, demonstrating the ability to send CAMs and DENMs generated by vehicles virtually traveling on the SUMO map over a real network. This emulator application can also receive CAMs and DENMs from the external world, making it useful for hardware-in-the-loop testing and evaluation.

Emulator Application Features:

Emulates N vehicles, each with its own Cooperative Awareness (CA) and Decentralised Environmental Notification (DEN) basic services.
Sends and receives CAM/DENM messages through a physical interface, facilitating real-world network communication.
Runs in real-time, ensuring proper handling of the specified number of vehicles without delays or slowdowns.
Communicates only with ASN.1 standard-compliant messages.


Usage:

Run the emulator application with the following command:

./ns3 run "v2x-emulator --interface=<interface name>"


Where <interface name> is the name of the physical interface on your PC where CAMs will be sent.

Interface Configuration:

The interface should be put in promiscuous mode for ns-3 compatibility, which can be achieved using the following commands:

sudo ip link set <interface name> promisc on


Promiscuous mode can be disabled with:

sudo ip link set <interface name> promisc off

---------------------------------------------------------------------------

### Interpreting results

While the ms-van3t is considered an innovative way to test real life scenarios of internet of vehicles protocols, it is undeniable that the architecture by which it is designed does not effortlessly permit an easy framework for creating new scenarios besides the ones already implemented in the code. Nevertheless we have tried to add an analysis layer that serves as a gateway to monitoring some metrics like the “number of CAM messages” and the “trajectory of communication”. 

The V2X emulator application permits the monitoring of the messages from an outside gateway being the network interface we have set up to control the flux  of communication between the vehicles.
---------------------------------------------------------------------------

### Areas of improvement

Improving the MS-VAN3T framework for simulating Internet of Vehicles (IoV) protocols such as 802.11p, NR-V2X, and C-V2X involves addressing key areas to enhance simulation accuracy and versatility. 

Firstly, optimising the realism of channel models is crucial for better reflecting real-world vehicular communication environments. Incorporating more realistic mobility patterns, considering dynamic obstacles, and capturing varying propagation conditions will provide a more accurate representation of IoV scenarios. 

Additionally, enhancing the protocol models for 802.11p, NR-V2X, and C-V2X to reflect the latest standards and advancements in vehicular communication is essential. This involves staying updated with the evolving specifications of these protocols and adapting the simulation accordingly. 

Furthermore, the inclusion of intelligent and adaptive traffic models can better mimic the intricate dynamics of vehicular networks, enabling more realistic assessments of communication performance in diverse traffic scenarios. 

Moreover, extending the simulation framework to support hybrid communication scenarios, where multiple protocols coexist, will offer a more comprehensive evaluation of IoV systems. 

Finally, incorporating mechanisms to simulate the impact of security and privacy protocols within the vehicular communication framework will contribute to a more holistic evaluation of IoV systems in terms of reliability and resilience against potential cyber threats. 

By focusing on these areas, the MS-VAN3T framework can evolve to provide a more accurate and versatile platform for simulating a wide range of IoV protocols and scenarios.
---------------------------------------------------------------------------

### Conclusion

The ms-van3t project successfully simulates V2V communication using three different technologies, showcasing the implementation of emergency vehicle alert systems and providing an emulator application for testing and evaluation in real-world network scenarios. The structured approach to code organisation and integration with SUMO ensures a comprehensive and efficient simulation environment for the Internet of Vehicles (IoV).
---------------------------------------------------------------------------


### Webography:

ms-van3t GitHub Repository:

https://github.com/ms-van3t-devs/ms-van3t/tree/master

Description: The official GitHub repository for the ms-van3t project. Contains the source code, documentation, and resources for the multi-stack VANET framework for ns-3.

NetApp Documentation on ECMP:

https://library.netapp.com/ecmdocs/ECMP1155586/html/GUID-3C690A8F-691A-45F2-BA1D-05F945E14515.html

Description: NetApp documentation providing information on the specified topic related to ECMP (Equal-Cost Multipath) networking.

ResearchGate - VANET Overview:

https://www.researchgate.net/figure/VANET-Overview-There-are-two-types-of-nodes-OBU-and-RSU-These-nodes-form-ad-hoc_fig1_283637695

Description: ResearchGate article illustrating an overview of VANET (Vehicular Ad Hoc Network) with a focus on the two types of nodes, OBU (On-Board Unit) and RSU (Road-Side Unit).

LinuxHint - Installing Wireshark on Ubuntu:

https://linuxhint.com/install_wireshark_ubuntu/

Description: LinuxHint article providing a guide on installing Wireshark on the Ubuntu operating system, offering insights into network packet analysis.

Project Guideline - Installing ms-van3t:

https://www.projectguideline.com/installing-ms-van3t-a-multi-stack-vanet-framework-for-ns-3/

Description: Project Guideline article offering a step-by-step guide on installing ms-van3t, a multi-stack VANET framework for ns-3, providing users with insights into the installation process.

