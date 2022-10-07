from analytics import Research
from config import *

if __name__ == "__main__":
    try:
        researcher = Research(file_path)
        data = researcher.file_reader(has_header=True)
        counts = researcher.calc.counts(data)
        fractions = researcher.calc.fractions(counts[0], counts[1])
        predict_random = researcher.analytics.predict_random(5)
        random_tails = sum([el[1] for el in predict_random])
        random_heads = sum([el[0] for el in predict_random])
        predict_last = researcher.analytics.predict_last()
        test_report = report.format(len(data), counts[1], counts[0],
                                    fractions[1], fractions[0],
                                    nmbr_of_steps, random_heads, random_tails)
        researcher.analytics.save_file(test_report, file_to_save)
        researcher.send_report(success, webhook, token, chat_id)
    except Exception as err:
        print(type(err).__name__, err, sep=': ')