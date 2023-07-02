import java.util.Scanner;

public class Fourth {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder stringBuilder = new StringBuilder();
        int q = scanner.nextInt();
        for (int i = 0; i < q; i++) {
            long l, r;
            l = scanner.nextLong();
            r = scanner.nextLong();
            if (r - l + 1 >= 6) {
                stringBuilder.append("9\n");
            }
            else {
                long left = l;
                int product = 1;
                for (int j = 0; j < r - l + 1; j++){
                    product *= (left % 9);
                    ++left;
                }
                if (product % 9 == 0) {
                    stringBuilder.append("9\n");
                }
                else {
                    stringBuilder.append(product % 9).append("\n");
                }
            }
        }
        System.out.print(stringBuilder);
        scanner.close();
    }
}