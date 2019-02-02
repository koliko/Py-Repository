public class Time {

    public static void main(String [] arg){

        int [] arrays = {13,132,232,55,1};
        ReturnAll(arrays);
    }

    public static int ReturnAll(int [] myFirstArray){
//        int temp = 0;
//        int size = myFirstArray.length;
//        for (int i = 0; i < size; i ++){
//
//           temp = myFirstArray[i];
//            System.out.println(temp);
//        }
//        return temp;
        int x = myFirstArray[0];
        myFirstArray[0] = myFirstArray[myFirstArray.length -1];
        myFirstArray[myFirstArray.length-1] = x;
        System.out.println(myFirstArray);
        return x;
    }
}
