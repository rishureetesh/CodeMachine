// Printing one to hundred
class PrintNumber{
    static int Number = 10;
    static int constant = 1;
    static void printToHundreds(int number){
        if (number-1 > 0){
            printToHundreds(number-1);
        }
        System.out.println("Number " + number);
    }
    public static void main(String[] args){
        printToHundreds(Number);
    }
}