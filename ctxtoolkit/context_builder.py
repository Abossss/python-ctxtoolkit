class ContextBuilder:
    """
    Context Builder - For creating structured AI contexts
    Uses a three-layer structure: core instruction layer, key information layer, supplementary reference layer
    """
    
    def __init__(self):
        self.core_instruction = None
        self.requirements = []
        self.key_infos = {}
        self.references = []
    
    def add_core_instruction(self, task: str, requirements: list = None):
        """
        Add core instruction
        
        Args:
            task: Core task description
            requirements: List of task requirements
        """
        if not isinstance(task, str):
            raise TypeError("task must be a string")
            
        if task.strip() == "":
            raise ValueError("task cannot be empty")
            
        if requirements is not None:
            if not isinstance(requirements, list):
                raise TypeError("requirements must be a list")
                
            # Verify each element in the list is a string
            for i, req in enumerate(requirements):
                if not isinstance(req, str):
                    raise TypeError(f"Element {i+1} in requirements must be a string")
        
        self.core_instruction = task.strip()
        self.requirements = requirements if requirements else []
        
    def add_key_info(self, key: str, value: str):
        """
        Add key information
        
        Args:
            key: Information key
            value: Information value
        """
        if not isinstance(key, str):
            raise TypeError("key must be a string")
            
        if not isinstance(value, str):
            raise TypeError("value must be a string")
            
        if not key.strip():
            raise ValueError("key cannot be empty")
            
        self.key_infos[key.strip()] = value
    
    def add_reference(self, content: str, title: str = None):
        """
        Add supplementary reference
        
        Args:
            content: Reference content
            title: Reference title (optional)
        """
        if not isinstance(content, str):
            raise TypeError("content must be a string")
            
        if title is not None and not isinstance(title, str):
            raise TypeError("title must be a string")
            
        if content.strip() == "":
            raise ValueError("content cannot be empty")
            
        # Process whitespace in title
        processed_title = title.strip() if title else None
        self.references.append((processed_title, content))
    
    def build(self) -> str:
        """
        Build the final context
        
        Returns:
            Structured context string
        """
        context_parts = []
        
        # 1. Core Instruction Layer
        if self.core_instruction:
            context_parts.append("[Core Instruction]")
            context_parts.append(self.core_instruction)
            
            if self.requirements:
                context_parts.append("Requirements:")
                for i, req in enumerate(self.requirements, 1):
                    context_parts.append(f"{i}. {req}")
            
            context_parts.append("")
        
        # 2. Key Information Layer
        if self.key_infos:
            context_parts.append("[Key Information]")
            for key, value in self.key_infos.items():
                context_parts.append(f"- {key}: {value}")
            context_parts.append("")
        
        # 3. Supplementary Reference Layer
        if self.references:
            context_parts.append("[Supplementary Reference]")
            for title, content in self.references:
                if title:
                    context_parts.append(f"{title}")
                context_parts.append(content)
            context_parts.append("")
        
        return "\n".join(context_parts).strip()
    
    def clear(self):
        """
        Clear all content and restart building
        """
        self.__init__()
