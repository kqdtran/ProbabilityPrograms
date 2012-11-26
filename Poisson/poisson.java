public class poisson {

    /** This function is based on Donald Knuth's algorithm for generating random Poisson number
     *  @param lambda - the mean of the Poisson random variable   
     */
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

    /** Calculate P(X >= lowerThreshold)
     *  @param lambda - the mean of the Poisson random variable
     *  @param lowerThreshold - the threshold you want to calculate the probability for
     *  @param numTimes - the number of times you want to run the simulation. 
     */  
    public static double calculatePoisson(double lambda, double lowerThreshold, int numTimesOneRun) {
        int random, total = 0;
        for (int k = 0; k < numTimesOneRun; k++) {
            random = poissonRandomNumber(lambda);
            if (random >= lowerThreshold)
                total += 1;
        }
        return (double) total / numTimesOneRun;
    }

    /**
     * Calculate the upper bound after running numRunUpperBound times
     */
    public static double calculateUpperBound(double lambda, double lowerThreshold, int numTimesOneRun, int numRunUpperBound) {
        double result;
        double upperBound = 0;
        for (int k = 0; k < numRunUpperBound; k++) {
            result = calculatePoisson(lambda, lowerThreshold, numTimesOneRun);
            if (result > upperBound)
                upperBound = result;
        }
        return upperBound;
    }

    public static void main(String [] args) {
        /* EDIT YOUR LAMBDA, THRESHOLD, NUMBER OF CALCULATION FOR EACH RUN, AND NUMBER OF RUNS HERE */
        double lambda = 20;
        double lowerThreshold = 26;
        int numTimesOneRun = 1000;
        int numRunUpperBound = 100;
        
        System.out.println("Simulate Poisson Random Process with lambda = " + lambda + " and lower threshold = " + lowerThreshold + " in " + numTimesOneRun + " runs");
        System.out.println("The upper bound after " + numRunUpperBound + " times is: " + calculateUpperBound(lambda, lowerThreshold, numTimesOneRun, numRunUpperBound));
    }
}
