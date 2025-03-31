# CST_8916_Final_Project

## Senario description

In the Rideau Canal during winter, there is a lot of people who skates on the canal. However, there could be a real issue that the ice can break and hurt a lot of skaters. Therefore, engineers implemented sensors to scan and calculate if the ice will be breaking. The sensors are in 3 locations: Dow's Lake, Fifth Avenue, and National Arts Center (NAC). The sensors monitor 4 values: ice thickness, surface temperature, snow accumulation, and external temperature. After it gets the values, it calculates to get the average ice thickness and maximum snow accumulation. This system is helpful to tell if the ice could break depending on the ice. The ice can break easily if either the ice thickness average is low, surface temperature is high, maximum snow accumulation is high, and external temperature is high. Therefore, we developed a real time system to track these changes.

## System Architecture

![alt text](Real_Time_System.drawio.png)

For this assignment, we don't have any actual real life sensors to gain the data. Instead, we use a python program to generate the data and send them to the sensors in the IoT Hub. In the program, it goes in a while loop to gain the data every 10 seconds. The data is generated randomly from 0 to 30 cm of the length data and -20 to 20 *C of the temprature data. There are 3 programs represents each location and they are connected to the sensors using a connection string. 

Examples of a json payload generated displayed bellow:

The application used to run these programs is visual studios connected to a virtual machine.

