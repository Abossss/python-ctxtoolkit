class AntiPollutionSystem:
    """
    Context Anti-Pollution System - Prevents context pollution
    Features: error content isolation, task boundary division, consistency checking
    """
    
    def __init__(self):
        self.task_boundary = "---"
        self.verified_marker = "[Verified]"
        self.unverified_marker = "[Unverified]"
    
    def create_task_boundary(self, task_name: str, content: str) -> str:
        """
        Create task boundary
        
        Args:
            task_name: Task name
            content: Task content
            
        Returns:
            Task content with boundaries
        """
        if not isinstance(task_name, str):
            raise TypeError("task_name must be a string")
            
        if not isinstance(content, str):
            raise TypeError("content must be a string")
            
        if not task_name.strip():
            raise ValueError("task_name cannot be empty")
            
        return f"{self.task_boundary}\n[{task_name.strip()}]\n{content}\n{self.task_boundary}"
    
    def mark_unverified(self, content: str) -> str:
        """
        Mark content as unverified
        
        Args:
            content: Content to mark
            
        Returns:
            Marked content
        """
        if not isinstance(content, str):
            raise TypeError("content must be a string")
            
        return f"{self.unverified_marker} {content}"
    
    def mark_verified(self, content: str) -> str:
        """
        Mark content as verified
        
        Args:
            content: Content to mark
            
        Returns:
            Marked content
        """
        if not isinstance(content, str):
            raise TypeError("content must be a string")
            
        return f"{self.verified_marker} {content}"
    
    def reset_context(self, new_instruction: str) -> str:
        """
        Reset context, ignoring all previous instructions
        
        Args:
            new_instruction: New instruction
            
        Returns:
            Reset context
        """
        if not isinstance(new_instruction, str):
            raise TypeError("new_instruction must be a string")
            
        if not new_instruction.strip():
            raise ValueError("new_instruction cannot be empty")
            
        return f"Ignore all previous instructions. Now please:\n{new_instruction}"
    
    def check_consistency(self, context1: str, context2: str) -> dict:
        """
        Check consistency between two contexts
        
        Args:
            context1: First context
            context2: Second context
            
        Returns:
            Consistency check results
        """
        if not isinstance(context1, str):
            raise TypeError("context1 must be a string")
            
        if not isinstance(context2, str):
            raise TypeError("context2 must be a string")
        
        import re
        from collections import Counter
        
        # 1. Check terminology consistency
        terms1 = set(re.findall(r'\[(\w+)\]', context1))
        terms2 = set(re.findall(r'\[(\w+)\]', context2))
        
        common_terms = terms1.intersection(terms2)
        unique_terms1 = terms1.difference(terms2)
        unique_terms2 = terms2.difference(terms1)
        
        # Calculate term consistency score
        total_terms = len(terms1) + len(terms2)
        term_consistency = len(common_terms) / max(total_terms, 1)
        
        # 2. Check keyword consistency
        def extract_keywords(text):
            """Extract keywords from text"""
            # Remove punctuation
            text = re.sub(r'[^\w\s]', '', text)
            # Convert to lowercase and split into words
            words = text.lower().split()
            # Filter stopwords
            stop_words = set(["的", "了", "和", "是", "在", "有", "为", "与", "而", "之一", "就", "都", " 但", "这", "a", "an", "the", "is", "are", "and", "or", "but"])
            keywords = [word for word in words if word not in stop_words and len(word) > 1]
            return Counter(keywords)

        keywords1 = extract_keywords(context1)
        keywords2 = extract_keywords(context2)
        
        common_keywords = set(keywords1.keys()) & set(keywords2.keys())
        total_keywords = set(keywords1.keys()) | set(keywords2.keys())

        # Calculate keyword consistency score
        keyword_consistency = len(common_keywords) / max(len(total_keywords), 1)

        # 3. Check instruction type consistency (simple check if both contain core instruction marker)
        has_instruction1 = "[Core Instruction]" in context1
        has_instruction2 = "[Core Instruction]" in context2
        instruction_consistency = 1.0 if has_instruction1 == has_instruction2 else 0.0

        # 4. Calculate overall consistency score
        overall_consistency = (term_consistency * 0.5 + keyword_consistency * 0.3 + instruction_consistency * 0.2)

        return {
            "term_analysis": {
                "common_terms": list(common_terms),
                "unique_in_context1": list(unique_terms1),
                "unique_in_context2": list(unique_terms2),
                "consistency_score": term_consistency
            },
            "keyword_analysis": {
                "common_keywords": list(common_keywords),
                "total_keywords": len(total_keywords),
                "consistency_score": keyword_consistency
            },
            "structure_analysis": {
                "both_have_instruction": has_instruction1 and has_instruction2,
                "consistency_score": instruction_consistency
            },
            "overall_consistency": overall_consistency
        }

    def isolate_error(self, error_content: str, main_content: str) -> str:
        """
        Isolate error content

        Args:
            error_content: Error content
            main_content: Main content

        Returns:
            Isolated content
        """
        if not isinstance(error_content, str):
            raise TypeError("error_content must be a string")

        if not isinstance(main_content, str):
            raise TypeError("main_content must be a string")

        return f"{main_content}\n\n[Note: The following content may contain errors, please use with caution]\n{error_content}"
