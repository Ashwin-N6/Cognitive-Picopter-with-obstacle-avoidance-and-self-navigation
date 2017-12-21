

f=open('1a.txt', 'r')
a=[map(int, line.split("\t")) for line in f]



for j in range (0,3):
    

 if a[j][0]>=(400):
  print "\nobstacle not found\n"

 else:
    print "obstacle found in North direction, Its at the distance of %d cms"%(a[j][0])


    if a[j][0]<=100:
     print "\n WARNING!!! OBSTACLE IS VERY NEAR!! \n"
     import random 
     def south():
        print "\n Change direction to South \n"

     def east():
         print "\n Change direction to East  \n"

     def west():
         print "\n Change direction to West \n"

     my_list = [south, east, west]
     random.choice(my_list)()


 if a[j][1]>= 400:
   print "\nobstacle not found\n"

 else:
    print "obstacle found in South direction, Its at the distance of %d cms"%(a[j][1])

    if a[j][1]<=100: 
      print " \nWARNING!!! OBSTACLE IS VERY NEAR!! \n"
      import random 
      def east():
         print "\n Change direction to East \n"

      def north():
         print "\n Change direction to North  \n"

      def west():
         print "\n Change direction to West \n"

      my_list = [east, north, west]
      random.choice(my_list)()


 if a[j][2]>= 400:
   print "\n obstacle not found\n"

 else:
    print "obstacle found in East direction, Its at the distance of %d cms"%(a[j][2])

    if a[j][2]<=100: 
      print " \nWARNING!!! OBSTACLE IS VERY NEAR!! \n"
      import random 
      def south():
         print "\n Change direction to South \n"

      def west():
         print "\n Change direction to West  \n"

      def east():
         print "\n Change direction to East \n"

      my_list = [south, east, west]
      random.choice(my_list)()

 if a[j][3]>= 400:
   print "\nobstacle not found\n"
 else:
    print "obstacle found in West direction, Its at the distance of %d cms"%(a[j][3])

    if a[j][3]<=100: 
      print "\n WARNING!!! OBSTACLE IS VERY NEAR!! \n"
      import random 
      def east():
        print "\n Change direction to East \n"

      def south():
        print "\n Change direction to South  \n"

      def north():
         print "\n Change direction to North \n"

      my_list = [south, east, north]
      random.choice(my_list)()

