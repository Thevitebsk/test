s=50;h=25;sub=5;l=0;ls=0;su=6
print("Student simulator")
def game():
    global s,h,sub,l,ls,su;print(f"Current status:\nsanity:{s}\nhunger:{h}\nsubjects left:{sub}\nlunchbox eaten?:{l}\nLearning time?:{ls}\nMinutes:{su}");a=input("What will you do now\n1.Play on your phone\n2.Eat your lunchbox\n3.Shake your head very fast\n")
    if a=="1" and ls==0:print("You took your phone out of your backpack and played in it and 15 minutes later the bell ringed and you put your phone down");ls=1;h-=1
    if a=="1" and ls==1:print("\"It's learning time and not playing time\" you whisper to yourself");s-=8;h-=1
    if a=="2" and ls==0 and l==0:print("You ate your lunch from the lunchbox and you don't fell very hungry anymore");h+=25;l=1;s-=8
    if a=="2" and ls==1 and l==0:print("\"Why couldn't i eaten my lunchbox before\" you whisper to yourself");h-=1;s-=8
    if a=="2" and ls==0 and l==1:print("You alredy ate your lunch");h-=1;s-=8
    if a=="2" and ls==1 and l==1:print("\"If i could eat my lunchbox\" you whisper to yourself");h-=1;s-=8
    if a=="3" and ls==0:print("You gained more sanity by just shaking your head very fast");h-=1;s+=14
    if a=="3" and ls==1:print("You gained more sanity by just shaking your head very fast");h-=1;s+=14
    if su==0:su=6;ls=0;sub-=1
    if s>100:print("\"I think i can handle it\" you whisper to yourself");s=100
    if ls==1 and a!="":su-=1
while s>0 or h>0 or sub>0:game()
