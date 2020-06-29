package ca;

import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.java.tuple.Tuple5;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class CategoryAggregation {
	public static void main(String[] args) throws Exception {
		final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
		DataStream<String> data = env.readTextFile("./Users/Timon/eclipse-workspace/SuperstoreReduced.txt");
		DataStream<Tuple5<String, String, String, Integer, Double>> mapped = data.map(new Splitter());

		mapped.keyBy(1).minBy(4).writeAsText("./Users/Timon/eclipse-workspace/min");
		mapped.keyBy(1).maxBy(4).writeAsText("./Users/Timon/eclipse-workspace/max");

		env.execute("Aggregation");
	}

	public static class Splitter implements MapFunction<String, Tuple5<String, String, String, Integer, Double>> {
		public Tuple5<String, String, String, Integer, Double> map(String value) {
			String[] words = value.split(",");
			return new Tuple5<String, String, String, Integer, Double>(words[0], words[1], words[2],
					Integer.parseInt(words[3]), Double.parseDouble(words[4]));
		}
	}
}
