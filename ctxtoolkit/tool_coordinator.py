class ToolCoordinator:
    """
    Tool Coordinator - For managing the collaboration of multiple tools
    Features: tool boundary definition, dynamic call constraints, multi-tool collaboration workflow
    """
    
    def __init__(self):
        self.tools = {}
        self.call_constraints = {}
        self.workflows = {}
    
    def register_tool(self, tool_name: str, description: str, capabilities: list):
        """
        Register tool
        
        Args:
            tool_name: Tool name
            description: Tool description
            capabilities: List of tool capabilities
        """
        if not isinstance(tool_name, str):
            raise TypeError("tool_name must be a string")
            
        if not isinstance(description, str):
            raise TypeError("description must be a string")
            
        if not isinstance(capabilities, list):
            raise TypeError("capabilities must be a list")
            
        if not tool_name.strip():
            raise ValueError("tool_name cannot be empty")
            
        # Verify each element in capabilities is a string
        for i, capability in enumerate(capabilities):
            if not isinstance(capability, str):
                raise TypeError(f"Element {i+1} in capabilities must be a string")
        
        self.tools[tool_name.strip()] = {
            "description": description,
            "capabilities": capabilities,
            "is_available": True
        }
    
    def set_tool_availability(self, tool_name: str, is_available: bool):
        """
        Set tool availability
        
        Args:
            tool_name: Tool name
            is_available: Whether the tool is available
        """
        if not isinstance(tool_name, str):
            raise TypeError("tool_name must be a string")
            
        if not isinstance(is_available, bool):
            raise TypeError("is_available must be a boolean")
            
        if not tool_name.strip():
            raise ValueError("tool_name cannot be empty")
            
        tool_name = tool_name.strip()
        if tool_name in self.tools:
            self.tools[tool_name]["is_available"] = is_available
        else:
            raise ValueError(f"Tool {tool_name} is not registered")
    
    def add_call_constraint(self, tool_name: str, constraint: callable):
        """
        Add tool call constraint
        
        Args:
            tool_name: Tool name
            constraint: Constraint function that returns True if callable, False otherwise
        """
        if not isinstance(tool_name, str):
            raise TypeError("tool_name must be a string")
            
        if not callable(constraint):
            raise TypeError("constraint must be callable")
            
        if not tool_name.strip():
            raise ValueError("tool_name cannot be empty")
            
        tool_name = tool_name.strip()
        if tool_name not in self.tools:
            raise ValueError(f"Tool {tool_name} is not registered")
            
        self.call_constraints[tool_name] = constraint
    
    def can_call_tool(self, tool_name: str, context: dict = None) -> bool:
        """
        Check if tool can be called
        
        Args:
            tool_name: Tool name
            context: Context information
            
        Returns:
            Whether the tool can be called
        """
        if not isinstance(tool_name, str):
            raise TypeError("tool_name must be a string")

        if context is not None and not isinstance(context, dict):
            raise TypeError("context must be a dictionary")

        if not tool_name.strip():
            raise ValueError("tool_name cannot be empty")

        tool_name = tool_name.strip()
        
        # Check if tool exists and is available
        if tool_name not in self.tools or not self.tools[tool_name]["is_available"]:
            return False

        # Check constraint conditions
        if tool_name in self.call_constraints:
            return self.call_constraints[tool_name](context or {})

        return True

    def define_workflow(self, workflow_name: str, steps: list):
        """
        Define workflow

        Args:
            workflow_name: Workflow name
            steps: Workflow steps list, each step contains tool_name and parameters
        """
        if not isinstance(workflow_name, str):
            raise TypeError("workflow_name must be a string")

        if not isinstance(steps, list):
            raise TypeError("steps must be a list")

        if not workflow_name.strip():
            raise ValueError("workflow_name cannot be empty")

        # Verify each step in steps
        for i, step in enumerate(steps):
            if not isinstance(step, dict):
                raise TypeError(f"Element {i+1} in steps must be a dictionary")

            if "tool_name" not in step:
                raise ValueError(f"Element {i+1} in steps is missing tool_name field")

            tool_name = step["tool_name"]
            if not isinstance(tool_name, str) or not tool_name.strip():
                raise ValueError(f"tool_name in element {i+1} of steps must be a non-empty string")

            if tool_name.strip() not in self.tools:
                raise ValueError(f"Element {i+1} in steps references unregistered tool {tool_name}")

            if "parameters" in step and not isinstance(step["parameters"], dict):
                raise TypeError(f"parameters in element {i+1} of steps must be a dictionary")

        self.workflows[workflow_name.strip()] = steps

    def execute_workflow(self, workflow_name: str, context: dict = None) -> dict:
        """
        Execute workflow

        Args:
            workflow_name: Workflow name
            context: Context information

        Returns:
            Execution results
        """
        if not isinstance(workflow_name, str):
            raise TypeError("workflow_name must be a string")

        if context is not None and not isinstance(context, dict):
            raise TypeError("context must be a dictionary")

        if not workflow_name.strip():
            raise ValueError("workflow_name cannot be empty")

        workflow_name = workflow_name.strip()

        if workflow_name not in self.workflows:
            return {
                "success": False,
                "error": f"Workflow {workflow_name} does not exist"
            }

        results = []
        current_context = context or {}

        for i, step in enumerate(self.workflows[workflow_name]):
            tool_name = step["tool_name"]
            parameters = step.get("parameters", {})

            if not self.can_call_tool(tool_name, current_context):
                return {
                    "success": False,
                    "error": f"Cannot call tool {tool_name}, workflow execution failed",
                    "completed_steps": results,
                    "step_number": i + 1
                }

            try:
                # In actual projects, this would call the real tool
                # Here we only simulate tool calling
                result = {
                    "step": i + 1,
                    "tool": tool_name,
                    "parameters": parameters,
                    "result": f"Simulated {tool_name} execution result"
                }

                results.append(result)
                current_context[f"step_{i+1}_result"] = result
            except Exception as e:
                return {
                    "success": False,
                    "error": f"Error occurred during step {i+1}: {str(e)}",
                    "completed_steps": results,
                    "step_number": i + 1
                }

        return {
            "success": True,
            "results": results,
            "total_steps": len(results)
        }

    def get_tool_info(self, tool_name: str) -> dict:
        """
        Get tool information

        Args:
            tool_name: Tool name

        Returns:
            Tool information
        """
        if not isinstance(tool_name, str):
            raise TypeError("tool_name must be a string")

        if not tool_name.strip():
            raise ValueError("tool_name cannot be empty")

        return self.tools.get(tool_name.strip(), {})

    def list_available_tools(self) -> list:
        """
        List available tools

        Returns:
            List of available tools
        """
        return [
            tool_name for tool_name, info in self.tools.items()
            if info["is_available"]
        ]
