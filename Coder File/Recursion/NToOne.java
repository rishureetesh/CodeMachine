class NToOne{
    static void printNToOne(int number){
        if(number == 0){
            return;
        }
        System.out.println(number);
        printNToOne(number-1);
    }
    public static void main(String[] args) {
        int Constant = 10;
        printNToOne(Constant);
    }
}