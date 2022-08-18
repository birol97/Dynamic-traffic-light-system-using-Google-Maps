#blink.py
import time
import RPi.GPIO as GPIO
status = True;
class traffic_light_cycle:
      lane1 = "lane1"
      lane2 = "lane2"
      lane3 = "lane3"
      fixed_red_cycle =  75
      fixed_yellow_cycle = 15
      fixed_green_cycle = 30
      last_cong_list = ();
      def __init__(self,lane_numb):
                   self.red = 75
                   self.yellow = 75
                   self.green = 75
                   self.lane_numb = lane_numb

      def store_last_received(lanes):

           global status
           last_cong_list.append(lanes);
           if len(last_cong_list) > 1:
              last_cong_list.pop(0);
           if status == True:
              print("status true")
              return receive_priority(last_cong_list[0]);
      def receive_priority(lanes):
            global status


            #array_values indicates congestion lane1,lane2,lane3


            for i in range(0,3):
                status = False;
                if lanes[0] > lanes[1] and lanes[0] > lanes[2]:

                   p1 = traffic_light_cycle(0);

                   lanes[0] = -1;
                   update_traffic_light_cycle(p1);
                   print("traffic_object_created")
                elif lanes[1] > lanes[2] and lanes[1] > lanes[0]:
                   p2 = traffic_light_cycle(1);
                   lanes[1] = -1;
                 update_traffic_light_cycle(p2);
                   print("traffic_object_created2")
                elif lanes[2] >= lanes[1] and lanes[2] >= lanes[0]:
                   p3 = traffic_light_cycle(2);
                   lanes[2] = -1;
                   update_traffic_light_cycle(p3);
                   print("traffic_object_created3")

            status = True;

            receive_priority(last_cong_list[0]);


            return 1;

      def getlane(traffic_cycle_object):
            return traffic_cycle_object.lane_numb;

      def update_traffic_light_cycle(traffic_cycle_object):
            lane = traffic_cycle_object.lane_numbl

            lane0_BCM_RED_PIN =   27
            lane0_BCM_YELLOW_PIN = 17
            lane0_BCM_GREEN_PIN  = 4


            lane1_BCM_RED_PIN =  5
            lane1_BCM_YELLOW_PIN = 6
            lane1_BCM_GREEN_PIN = 13


            lane2_BCM_RED_PIN =  10
            lane2_BCM_YELLOW_PIN = 9
            lane2_BCM_GREEN_PIN = 11


            GPIO.setmode(GPIO.BCM)
            GPIO.setup()
            if(lane == 0):
                print("Current lane1 is green");
                GPIO.setup(lane0_BCM_GREEN_PIN,GPIO_HIGH);
                GPIO.setup(lane1_BCM_GREEN_PIN,GPIO_LOW);
                GPIO.setup(lane2_BCM_GREEN_PIN,GPIO_LOW);

                

                GPIO.setup(lane0_BCM_YELLOW_PIN,GPIO_LOW);
                GPIO.setup(lane1_BCM_YELLOW_PIN,GPIO_LOW);
                GPIO.setup(lane2_BCM_YELLOW_PIN,GPIO_LOW);

                GPIO.setup(lane0_BCM_RED_PIN,GPIO_LOW);
                GPIO.setup(lane1_BCM_RED_PIN,GPIO_HIGH);
                GPIO.setup(lane2_BCM_RED_PIN,GPIO_HIGH);

                sleep(fixed_green_cycle);



            elif(lane == 1):
                print("Current lane2 is green")
                GPIO.setup(lane0_BCM_GREEN_PIN,GPIO_LOW);
                GPIO.setup(lane1_BCM_GREEN_PIN,GPIO_HIGH);
                GPIO.setup(lane2_BCM_GREEN_PIN,GPIO_LOW);

                GPIO.setup(lane0_BCM_YELLOW_PIN,GPIO_LOW);
                GPIO.setup(lane1_BCM_YELLOW_PIN,GPIO_LOW);
                GPIO.setup(lane2_BCM_YELLOW_PIN,GPIO_LOW);

                GPIO.setup(lane0_BCM_RED_PIN,GPIO_HIGH);
                GPIO.setup(lane1_BCM_RED_PIN,GPIO_LOW);
                GPIO.setup(lane2_BCM_RED_PIN,GPIO_HIGH);

                sleep(fixed_green_cycle);

                print("Current lane3 is green")
            elif(lane == 2):
                GPIO.setup(lane0_BCM_GREEN_PIN,GPIO_LOW);
                GPIO.setup(lane1_BCM_GREEN_PIN,GPIO_LOW);
                GPIO.setup(lane2_BCM_GREEN_PIN,GPIO_HIGH);

                GPIO.setup(lane0_BCM_YELLOW_PIN,GPIO_LOW);
                GPIO.setup(lane1_BCM_YELLOW_PIN,GPIO_LOW);
                GPIO.setup(lane2_BCM_YELLOW_PIN,GPIO_LOW);

                GPIO.setup(lane0_BCM_RED_PIN,GPIO_HIGH);
                GPIO.setup(lane1_BCM_RED_PIN,GPIO_HIGH);
                GPIO.setup(lane2_BCM_RED_PIN,GPIO_LOW);

                sleep(fixed_green_cycle);


            return 1
      def get_red_value(traffic_cycle_object):

            return traffic_cycle_object.red
      def get_yellow_value(traffic_cycle_object):

            return traffic_cycle_object.yellow
      def get_green_value(traffic_cycle_object):

            return traffic_cycle_object.green;
      def get_lane_status():
            return 1;
      def get_timer():
            print("Still in the cycle current time left is " +  timer)
            return timer;
   
                   
                   
                   
                   
                   
                   
