import os
import cv2

list_of_names = []


# def delete_old_data():
#    for i in os.listdir("pictures/"):
#       os.remove("pictures/{}".format(i))


def cleanup_data():
   with open('n.txt') as f:
      for line in f:
          list_of_names.append(line.strip())


def generate_certificates():
   cert = "Certificate No- FW/CC/C++/8790"

   for index, name in enumerate(list_of_names):
      certificate_template_image = cv2.imread("template2.png")
      cv2.putText(certificate_template_image, name.strip(), (122,730), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10, cv2.LINE_AA)
      cv2.putText(certificate_template_image, cert + "90", (1100,20), cv2.FONT_HERSHEY_PLAIN, 1, (246, 183, 169 ), 2, cv2.LINE_AA)
      cv2.imwrite("pictures/{}.jpg".format(name.strip()), certificate_template_image)
      print("Processing {} / {}".format(index + 1,len(list_of_names)))
      


def main():
   # delete_old_data()
   cleanup_data()
   generate_certificates()



if __name__ == '__main__':
   main()
