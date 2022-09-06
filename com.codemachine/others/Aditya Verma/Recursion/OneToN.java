class OneToN{
    static void printOneToN(int number){
        if(number == 0){
            return;
        }
        printOneToN(number-1);
        System.out.println(number);
    }
    public static void main(String[] args) {
        int Constant = 10;
        printOneToN(Constant);
    }
}