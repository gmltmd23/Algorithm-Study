import java.util.*;

public class Main {
    static class ParkingInfo {
        public int hour;
        public int minute;
        public int total;

        public ParkingInfo(int hour, int minute) {
            this.hour = hour;
            this.minute = minute;
            this.total = 0;
        }

        public void setHourAndMinute(int hour, int minute) {
            this.hour = hour;
            this.minute = minute;
        }

        public void calculateTime(int hour, int minute) {
            if(this.hour == hour) {
                this.total += (minute - this.minute);
            }
            else {
                if(minute > this.minute)
                    this.total += ((hour - this.hour) * 60) + (minute - this.minute);
                else
                    this.total += ((hour - this.hour) * 60) - (this.minute - minute);
            }
        }

        public boolean isInCar() {
            if(this.hour == -1 && this.minute == -1)
                return false;
            return true;
        }
    }

    public static int[] solution(int[] fees, String[] records) {
        HashMap<String, ParkingInfo> parkingMap = new HashMap<>();
        for(String record : records) {
            String[] splitedRecord = record.split(" ");
            String[] splitedTime = splitedRecord[0].split(":");

            int hour = Integer.parseInt(splitedTime[0]);
            int minute = Integer.parseInt(splitedTime[1]);
            String carNumber = splitedRecord[1];

            if(!parkingMap.containsKey(carNumber))
                parkingMap.put(carNumber, new ParkingInfo(-1, -1));

            ParkingInfo nowParkingInfo = parkingMap.get(carNumber);
            if(!nowParkingInfo.isInCar()) {
                nowParkingInfo.setHourAndMinute(hour, minute);
            }
            else {
                nowParkingInfo.calculateTime(hour, minute);
                nowParkingInfo.setHourAndMinute(-1, -1);
            }
        }

        ArrayList<String> carNumberList = new ArrayList<>();
        for(String carNumber : parkingMap.keySet()) {
            carNumberList.add(carNumber);
            ParkingInfo nowParkingInfo = parkingMap.get(carNumber);

            if(nowParkingInfo.isInCar())
                nowParkingInfo.calculateTime(23, 59);
        }

        Collections.sort(carNumberList);
        int[] result = new int[carNumberList.size()];
        for(int i = 0; i < result.length; ++i) {
            String carNumber = carNumberList.get(i);
            int total = parkingMap.get(carNumber).total;
            double value = (double)(total - fees[0]) / fees[2];
            if(value < 0)
                value = 0;
            result[i] = (int)(fees[1] + ( Math.ceil(value) * fees[3] ));
        }

        return result;
    }

    public static void main(String[] args) {
        int[] fees = {180, 5000, 10, 600};
        String[] records = {"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"};
        System.out.println(solution(fees, records));
    }
}