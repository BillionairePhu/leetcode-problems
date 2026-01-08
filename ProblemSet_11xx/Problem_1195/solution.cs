public class FizzBuzz {
    private int n;
    private int index;
    private System.Threading.Lock printLock = new();

    public FizzBuzz(int n) {
        this.n = n;
    }

    // printFizz() outputs "fizz".
    public void Fizz(Action printFizz) {
        while (true)
        {
            lock (printLock) if (index % 3 == 0 && index % 5 == 0 && index <= n)
            {
                printFizz();    
                index++;
            }
        }
    }

    // printBuzzz() outputs "buzz".
    public void Buzz(Action printBuzz) {
        while (true)
        {
            lock (printLock) if (index % 3 == 0 && index % 5 != 0 && index <= n)
            {
                printBuzz();    
                index++;
            }
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
    public void Fizzbuzz(Action printFizzBuzz) {
        while (true){
            lock (printLock) if (index % 3 != 0 && index % 5 == 0 && index <= n)
            {
                printFizzBuzz();    
                index++;
            }
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    public void Number(Action<int> printNumber) {
        while (true)
        {
            lock (printLock) if (index % 3 != 0 && index % 5 != 0 && index <= n)
            {
                printNumber(index);    
                index++;
            }
        }
    }
}