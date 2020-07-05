package cp;

import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.common.functions.ReduceFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.api.java.tuple.Tuple5;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class CategoryProfit {
	public static void main(String[] args) throws Exception {
		final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
		DataStream<String> data = env.readTextFile("./Users/Timon/eclipse-workspace/SuperstoreReduced.txt");
		DataStream<Tuple5<String, String, String, Integer, Double>> mapped = data.map(new Splitter());
		DataStream<Tuple5<String, String, String, Integer, Double>> reduced = mapped.keyBy(1).reduce(new Reduce1());
		DataStream<Tuple2<String, Double>> profitPerCategory = reduced
				.map(new MapFunction<Tuple5<String, String, String, Integer, Double>, Tuple2<String, Double>>() {
					public Tuple2<String, Double> map(Tuple5<String, String, String, Integer, Double> input) {
						return new Tuple2<String, Double>(input.f1, input.f4);
					}
				});

		profitPerCategory.print();
		
		env.execute("Profit per category");
	}

	public static class Reduce1 implements ReduceFunction<Tuple5<String, String, String, Integer, Double>> {
		public Tuple5<String, String, String, Integer, Double> reduce(
				Tuple5<String, String, String, Integer, Double> current,
				Tuple5<String, String, String, Integer, Double> pre_result) {
			return new Tuple5<String, String, String, Integer, Double>(current.f0, current.f1, current.f2,
					current.f3 + pre_result.f3, current.f4 + pre_result.f4);
		}
	}

	public static class Splitter implements MapFunction<String, Tuple5<String, String, String, Integer, Double>> {
		public Tuple5<String, String, String, Integer, Double> map(String value) {
			String[] words = value.split(",");
			return new Tuple5<String, String, String, Integer, Double>(words[0], words[1], words[2],
					Integer.parseInt(words[3]), Double.parseDouble(words[4]));
		}
	}
}
