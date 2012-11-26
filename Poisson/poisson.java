public class poisson {

    /** This is based off Donald Knuth's algorithm for generating random Poisson number */
    public static int poissonRandomNumber(double lambda) {
        double L = Math.exp(-lambda);
        int k = 0;
        double p = 1;
        
        do {
            k = k + 1;
            double u = Math.random();
            p = p * u;
        } while (p > L);
        
        return k - 1;
    }

    /** Calculate the probability of getting a value bigger than the lowerThreshold for a Poisson random variable 
     *  @param lambda - the mean of the Poisson random variable
     *  @param lowerThreshold - the value you want to calculate the probability for, e.g. P(X >= lowerThreshold)
     *  @param numTimes - the number of times you want to run the simulation. The higher numTimes is, the more accurate the result will be
     */
    
    public static double calculatePoisson(double lambda, double lowerThreshold, int numTimes) {
        int random, total = 0;
        for (int k = 0; k < numTimes; k++) {
            random = poissonRandomNumber(lambda);
            if (random >= lowerThreshold)
                total += 1;
        }
        return (double) total / numTimes;
    }

    public static void main(String [] args) {
        /* I don't use Scanner for input because it takes too much time to simulate a run when you have to enter those values each time. */
        /* EDIT YOUR LAMBDA, UPPER_BOUND, AND NUMBER OF RUNS HERE */
        double lambda = 20;
        double lowerThreshold = 26;
        int numTimes = 1000;
        
        System.out.print("Simulate Poisson Random Process with lambda = " + lambda + " and lower threshold = " + lowerThreshold + " in " + numTimes + " runs: ");
        System.out.println(calculatePoisson(20, 26, 1000));
    }
}
