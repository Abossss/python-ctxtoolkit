class TokenSaver:
    """
    Token Saver - For reducing Token consumption in contexts
    Features: terminology management, duplicate content merging, content compression
    """
    
    def __init__(self):
        self.terminology = {}
    
    def add_terminology(self, key: str, definition: str):
        """
        Add terminology definition
        
        Args:
            key: Terminology abbreviation/number
            definition: Complete terminology definition
        """
        if not isinstance(key, str):
            raise TypeError("key must be a string")
            
        if not isinstance(definition, str):
            raise TypeError("definition must be a string")
            
        if not key.strip():
            raise ValueError("key cannot be empty")
            
        self.terminology[key.strip()] = definition
    
    def add_terminologies(self, terms: dict):
        """
        Add multiple terminology definitions
        
        Args:
            terms: Dictionary of terms, where key is the abbreviation/number and value is the complete definition
        """
        if not isinstance(terms, dict):
            raise TypeError("terms must be a dictionary")
            
        # Validate dictionary content
        for key, definition in terms.items():
            if not isinstance(key, str) or not key.strip():
                raise ValueError(f"Invalid term key: {key}")
                
            if not isinstance(definition, str):
                raise TypeError(f"Definition for term {key} must be a string")
        
        # Process whitespace in keys
        processed_terms = {key.strip(): definition for key, definition in terms.items()}
        self.terminology.update(processed_terms)
    
    def build_compact_context(self, instruction: str, data: list = None, rules: list = None) -> str:
        """
        Build compact context
        
        Args:
            instruction: Core instruction
            data: List of related data
            rules: List of rules to follow
            
        Returns:
            Compact context string
        """
        if not isinstance(instruction, str):
            raise TypeError("instruction must be a string")
            
        if not instruction.strip():
            raise ValueError("instruction cannot be empty")
            
        if data is not None and not isinstance(data, list):
            raise TypeError("data must be a list")
            
        if rules is not None and not isinstance(rules, list):
            raise TypeError("rules must be a list")
            
        # Check if all rules are defined
        if rules:
            undefined_rules = [rule for rule in rules if rule not in self.terminology]
            if undefined_rules:
                raise ValueError(f"Undefined rules: {', '.join(undefined_rules)}")
        
        context_parts = []
        
        # Add terminology list
        if rules:
            context_parts.append("[Terminology]")
            for rule_key in rules:
                if rule_key in self.terminology:
                    context_parts.append(f"[{rule_key}] {self.terminology[rule_key]}")
            context_parts.append("")
        
        # Add core instruction
        context_parts.append(instruction)
        
        # Add rule reference
        if rules:
            context_parts[-1] += f", follow {', '.join(rules)}"
        
        context_parts.append("")
        
        # Add data
        if data:
            context_parts.append("Data:")
            for item in data:
                context_parts.append(str(item))
        
        return "\n".join(context_parts).strip()
    
    def merge_duplicates(self, content: str) -> str:
        """
        Merge duplicate content
        
        Args:
            content: Original content

        Returns:
            Content with duplicates merged
        """
        if not isinstance(content, str):
            raise TypeError("content must be a string")

        if content.strip() == "":
            return ""

        lines = content.split('\n')
        seen = set()
        unique_lines = []

        for line in lines:
            stripped = line.strip()
            if stripped and stripped not in seen:
                seen.add(stripped)
                unique_lines.append(line)

        return "\n".join(unique_lines)

    def compress_terms(self, content: str) -> str:
        """
        Compress content using terminology table

        Args:
            content: Original content

        Returns:
            Compressed content
        """
        if not isinstance(content, str):
            raise TypeError("content must be a string")

        if not self.terminology:
            return content

        compressed = content
        import re

        # Sort terms by length descending to avoid partial matching
        sorted_terms = sorted(
            self.terminology.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )

        for key, definition in sorted_terms:
            if not definition:
                continue

            # Use regex for exact matching, avoid partial matching
            # For Chinese text, remove \b word boundaries since Chinese doesn't have space-separated words
            try:
                # For definitions containing Chinese characters, don't use word boundaries
                if any('\u4e00' <= c <= '\u9fff' for c in definition):
                    pattern = re.compile(re.escape(definition))
                else:
                    pattern = re.compile(rf'\b{re.escape(definition)}\b')
                compressed = pattern.sub(f"[{key}]", compressed)
            except re.error:
                # Fall back to simple replacement if regex compilation fails
                if definition in compressed:
                    compressed = compressed.replace(definition, f"[{key}]")

        return compressed

    def clear_terminology(self):
        """
        Clear all terminology
        """
        self.terminology = {}

    def generate_summary(self, content: str, max_length: int = 100, method: str = "keyphrase") -> str:    
        """
        Generate content summary

        Args:
            content: Original content
            max_length: Maximum length of summary
            method: Summary method, supports "keyphrase" (keyword extraction) and "first_sentences" (first sentence summary)

        Returns:
            Generated summary
        """
        if not isinstance(content, str):
            raise TypeError("content must be a string")

        if not isinstance(max_length, int) or max_length <= 0:
            raise ValueError("max_length must be a positive integer")

        if content.strip() == "":
            return ""

        # Simple summary implementation
        if method == "first_sentences":
            # Summary based on first sentences
            sentences = content.split('.')
            summary = []
            current_length = 0

            for sentence in sentences:
                sentence = sentence.strip()
                if not sentence:
                    continue

                # Calculate total length after adding this sentence (including separators and ending punctuation)
                sentence_length = len(sentence)
                if summary:
                    # Need to add separator if there are existing sentences
                    sentence_length += 2  # ". "

                if current_length + sentence_length <= max_length:
                    summary.append(sentence)
                    current_length += sentence_length
                else:
                    # Truncate partial sentence
                    remaining = max_length - current_length
                    if remaining > 3:
                        # Add separator if needed
                        if summary:
                            remaining -= 2
                        if remaining > 3:
                            truncated = sentence[:remaining-3] + "..."
                            if summary:
                                summary.append(truncated)
                            else:
                                summary = [truncated]
                    break

            result = ". ".join(summary)
            # Ensure total length doesn't exceed limit
            if len(result) > max_length:
                result = result[:max_length-3] + "..."
            return result

        elif method == "keyphrase":
            # Summary based on keyword extraction
            import re
            from collections import Counter

            # Remove punctuation
            text = re.sub(r'[^\w\s]', '', content)

            # Extract keywords
            words = text.lower().split()
            word_counts = Counter(words)

            # Filter stopwords
            stop_words = set(["的", "了", "和", "是", "在", "有", "为", "与", "而", "之一", "就", "都", " 但", "这"])
            keywords = [word for word, count in word_counts.most_common(20) if word not in stop_words and len(word) > 1]

            # Generate summary
            summary = []
            current_length = 0

            for keyword in keywords:
                if current_length + len(keyword) + 4 <= max_length:
                    # Find sentences containing the keyword
                    sentences = re.split(r'[。！？]', content)
                    for sentence in sentences:
                        if keyword in sentence:
                            # Extract phrase containing the keyword
                            parts = sentence.split(keyword)
                            if len(parts) > 1:
                                phrase = parts[0].split()[-3:] + [keyword] + parts[1].split()[:3]
                                phrase = " ".join(filter(None, phrase))
                                summary.append(phrase)
                                current_length += len(phrase) + 2
                                break

            if not summary:
                # If no keywords extracted, use first sentence summary
                return self.generate_summary(content, max_length, method="first_sentences")

            # Merge summary and truncate if necessary
            full_summary = "; ".join(summary)
            if len(full_summary) <= max_length:
                return full_summary
            else:
                return full_summary[:max_length-3] + "..."

        else:
            raise ValueError("Unsupported summary method, only 'keyphrase' and 'first_sentences' are supported")
