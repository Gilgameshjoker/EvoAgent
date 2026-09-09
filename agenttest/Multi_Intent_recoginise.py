class MultiIntentRecognizer:
    """多意图识别器"""

    def __init__(self):
        self.single_recognizer = IntentRecognitionEngine()

    def split_sentence(self, text):
        """拆分复合句子"""
        # 使用连词分割
        separators = ['然后', '接着', '还有', '另外', '以及', '和']

        parts = [text]
        for sep in separators:
            new_parts = []
            for part in parts:
                new_parts.extend(part.split(sep))
            parts = new_parts

        return [p.strip() for p in parts if p.strip()]

    def recognize(self, text):
        """识别多意图"""
        # 拆分句子
        parts = self.split_sentence(text)

        # 识别每个部分的意图
        results = []
        for i, part in enumerate(parts):
            result = self.single_recognizer.process(part)
            result['sequence'] = i + 1
            results.append(result)

        return {
            "has_multiple_intents": len(results) > 1,
            "intents": results
        }


# 测试
multi_recognizer = MultiIntentRecognizer()
text = "帮我查明天北京天气，然后订张去上海的票"
result = multi_recognizer.recognize(text)

print("多意图识别结果:")
for intent in result['intents']:
    print(f"  意图{intent['sequence']}: {intent['intent']}")
