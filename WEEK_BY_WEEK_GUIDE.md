# Python Mastery: Week-by-Week Implementation Guide
## Actionable Lessons & Exercises

---

## WEEK 1: FOUNDATIONS & SETUP

### Day 1-2: Professional Environment

**Objectives:**
- Set up production-quality development environment
- Understand Python project structure
- Initialize version control

**Task 1: Environment Setup**
```bash
# Create project directory
mkdir python_mastery && cd python_mastery

# Initialize git
git init
git config user.name "Your Name"
git config user.email "your@email.com"

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

# Create requirements.txt
cat > requirements.txt << 'EOF'
black==23.12.1
pylint==3.0.0
pytest==7.4.3
pytest-cov==4.1.0
mypy==1.7.1
flake8==6.1.0
ipython==8.18.1
EOF

pip install -r requirements.txt
```

**Task 2: Project Structure**
```
python_mastery/
├── .git/
├── .gitignore
├── venv/
├── requirements.txt
├── README.md
├── setup.py
├── src/
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_*.py
├── docs/
│   └── API.md
└── .pylintrc
```

**Task 3: Configure Tools**

`.flake8`:
```ini
[flake8]
max-line-length = 100
extend-ignore = E203, W503
exclude = venv,__pycache__,build,dist
```

`.pylintrc` (generate with `pylint --generate-rcfile > .pylintrc` and modify for 100 char lines)

`pyproject.toml` (for Black):
```toml
[tool.black]
line-length = 100
target-version = ['py311']
```

**Task 4: Pre-commit Hooks**
```bash
pip install pre-commit

cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
  - repo: https://github.com/pylint-dev/pylint
    rev: pylint-3.0.0
    hooks:
      - id: pylint
        args: ['--disable=C0111']
EOF

pre-commit install
```

**Exercise 1.1:**
Create `src/hello.py`:
```python
"""
Module demonstrating professional Python code.

This module showcases best practices for Python development:
- Type hints
- Docstrings
- Proper error handling
- Logging
"""

import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Greeter:
    """A simple greeter class demonstrating OOP."""

    def __init__(self, name: str) -> None:
        """Initialize greeter with a name.

        Args:
            name: The name of the person to greet

        Raises:
            ValueError: If name is empty
        """
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        self.name = name
        logger.info(f"Greeter initialized for {name}")

    def greet(self, greeting: Optional[str] = None) -> str:
        """Create a greeting message.

        Args:
            greeting: Optional custom greeting prefix

        Returns:
            A formatted greeting message
        """
        prefix = greeting or "Hello"
        return f"{prefix}, {self.name}!"


def main() -> None:
    """Main entry point."""
    greeter = Greeter("Python Developer")
    print(greeter.greet())


if __name__ == "__main__":
    main()
```

Run linters:
```bash
black src/hello.py
pylint src/hello.py
flake8 src/hello.py
mypy src/hello.py  # Install: pip install mypy
```

---

### Day 3-5: Core Data Types Deep Dive

**Objectives:**
- Master Python's data model
- Understand type system
- Learn efficient data structure usage

**Exercise 1.2: Data Types Mastery**

Create `src/data_types.py`:
```python
"""Comprehensive data types and operations."""

from typing import Any, List, Dict, Tuple
import json
from collections import namedtuple, defaultdict, Counter


def demonstrate_strings() -> None:
    """String operations and methods."""
    s = "Python Programming"
    
    # String operations
    print(f"Original: {s}")
    print(f"Uppercase: {s.upper()}")
    print(f"Slicing: {s[:6]}")
    print(f"Split: {s.split()}")
    
    # f-strings (recommended over %)
    name, value = "Python", 3.11
    print(f"{name} version {value}")
    
    # String encoding
    text = "Hello, 世界"
    encoded = text.encode('utf-8')
    print(f"Bytes: {encoded}")


def demonstrate_collections() -> None:
    """Advanced collection operations."""
    # List comprehension
    squares = [x**2 for x in range(10)]
    print(f"Squares: {squares}")
    
    # Dictionary comprehension
    word_lengths = {word: len(word) for word in ["python", "code", "design"]}
    print(f"Word lengths: {word_lengths}")
    
    # Set operations
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print(f"Union: {set_a | set_b}")
    print(f"Intersection: {set_a & set_b}")
    
    # Named tuples
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"Point: x={p.x}, y={p.y}")


def demonstrate_advanced_dicts() -> None:
    """Advanced dictionary patterns."""
    # defaultdict for counting
    words = "python is powerful python".split()
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    print(f"Word count: {dict(word_count)}")
    
    # Counter is even more specialized
    counter = Counter(words)
    print(f"Counter: {counter.most_common(2)}")


def process_json_data() -> Dict[str, Any]:
    """Work with JSON data structures."""
    json_str = '''
    {
        "users": [
            {"id": 1, "name": "Alice", "active": true},
            {"id": 2, "name": "Bob", "active": false}
        ]
    }
    '''
    
    data = json.loads(json_str)
    
    # Transform data
    active_users = [u for u in data["users"] if u["active"]]
    print(f"Active users: {active_users}")
    
    return data


if __name__ == "__main__":
    demonstrate_strings()
    print()
    demonstrate_collections()
    print()
    demonstrate_advanced_dicts()
    print()
    process_json_data()
```

**Exercise 1.3: Data Validation**

Create `tests/test_data_types.py`:
```python
"""Tests for data types module."""

import pytest
from src.data_types import demonstrate_strings, process_json_data


def test_json_processing():
    """Test JSON data processing."""
    data = process_json_data()
    assert len(data["users"]) == 2
    assert data["users"][0]["name"] == "Alice"
```

Run: `pytest tests/ -v`

---

## WEEK 2-3: FUNCTIONS & FUNCTIONAL PROGRAMMING

### Exercise 2.1: Decorators for Logging

Create `src/decorators.py`:
```python
"""Professional decorators for production use."""

import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)


def timing_decorator(func: Callable) -> Callable:
    """Decorator to measure function execution time.
    
    Usage:
        @timing_decorator
        def slow_function(): 
            time.sleep(1)
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper


def retry_decorator(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry failed function calls with exponential backoff.
    
    Usage:
        @retry_decorator(max_attempts=3)
        def api_call():
            pass
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    wait = delay * (2 ** attempt)
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {wait}s")
                    time.sleep(wait)
        return wrapper
    return decorator


def cache_decorator(func: Callable) -> Callable:
    """Simple caching decorator (use functools.lru_cache in production)."""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


# Production use
@timing_decorator
def expensive_calculation(n: int) -> int:
    """Example function with timing."""
    return sum(i**2 for i in range(n))


if __name__ == "__main__":
    expensive_calculation(1000000)
```

---

### Exercise 2.2: Functional Programming Patterns

Create `src/functional.py`:
```python
"""Functional programming patterns in Python."""

from typing import List, Callable, Any
from functools import reduce
import operator


def filter_and_map_example(numbers: List[int]) -> List[int]:
    """Filter even numbers, map to squares."""
    # Imperative
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n ** 2)
    
    # Functional (preferred)
    result_func = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    
    # Even better: comprehension
    result_comp = [x**2 for x in numbers if x % 2 == 0]
    
    return result_comp


def compose_functions(*funcs: Callable) -> Callable:
    """Compose multiple functions: f(g(h(x)))."""
    def inner(arg: Any) -> Any:
        return reduce(lambda x, f: f(x), reversed(funcs), arg)
    return inner


def pipe(*funcs: Callable) -> Callable:
    """Pipe functions left-to-right: h(g(f(x)))."""
    def inner(arg: Any) -> Any:
        return reduce(lambda x, f: f(x), funcs, arg)
    return inner


# Example usage
add_one = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

# Compose: (square ∘ double ∘ add_one)(5) = square(double(add_one(5)))
result = compose_functions(square, double, add_one)(5)
print(f"Compose result: {result}")  # (2*6)^2 = 144

# Pipe: (add_one → double → square)(5)
result2 = pipe(add_one, double, square)(5)
print(f"Pipe result: {result2}")  # ((5+1)*2)^2 = 144
```

---

## WEEK 4-5: OOP & DESIGN PATTERNS

### Exercise 4.1: Class Design

Create `src/models.py`:
```python
"""Data models using modern Python features."""

from dataclasses import dataclass, field
from typing import List, Optional
from abc import ABC, abstractmethod
from enum import Enum
import json


class Status(Enum):
    """Status enumeration."""
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"


@dataclass
class User:
    """User model with automatic __init__, __repr__, __eq__."""
    name: str
    email: str
    status: Status = Status.ACTIVE
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Validation after initialization."""
        if '@' not in self.email:
            raise ValueError("Invalid email")
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "email": self.email,
            "status": self.status.value,
            "tags": self.tags,
        }


class Repository(ABC):
    """Abstract base class for data repositories."""
    
    @abstractmethod
    def get(self, id: int) -> Optional[User]:
        """Retrieve a user."""
        pass
    
    @abstractmethod
    def save(self, user: User) -> None:
        """Save a user."""
        pass


class InMemoryRepository(Repository):
    """In-memory user repository."""
    
    def __init__(self):
        self.users: dict = {}
        self.counter = 0
    
    def get(self, id: int) -> Optional[User]:
        return self.users.get(id)
    
    def save(self, user: User) -> None:
        self.counter += 1
        self.users[self.counter] = user


# Factory pattern
class UserFactory:
    """Factory for creating users."""
    
    @staticmethod
    def create_admin(name: str, email: str) -> User:
        user = User(name=name, email=email)
        user.tags.append("admin")
        return user
    
    @staticmethod
    def create_regular(name: str, email: str) -> User:
        return User(name=name, email=email)
```

---

### Exercise 4.2: Design Patterns

Create `src/patterns.py`:
```python
"""Common design patterns."""

from typing import Dict, Any
from abc import ABC, abstractmethod


# Singleton Pattern
class Config:
    """Configuration singleton."""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings: Dict[str, Any] = {}
        return cls._instance
    
    def set(self, key: str, value: Any) -> None:
        self.settings[key] = value
    
    def get(self, key: str) -> Any:
        return self.settings.get(key)


# Observer Pattern
class EventEmitter:
    """Simple event emitter."""
    
    def __init__(self):
        self.listeners: Dict[str, list] = {}
    
    def on(self, event: str, callback) -> None:
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(callback)
    
    def emit(self, event: str, data: Any) -> None:
        if event in self.listeners:
            for callback in self.listeners[event]:
                callback(data)


# Strategy Pattern
class PaymentStrategy(ABC):
    """Abstract payment strategy."""
    
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class CreditCardPayment(PaymentStrategy):
    """Credit card payment."""
    
    def pay(self, amount: float) -> bool:
        print(f"Processing credit card payment: ${amount}")
        return True


class PaypalPayment(PaymentStrategy):
    """PayPal payment."""
    
    def pay(self, amount: float) -> bool:
        print(f"Processing PayPal payment: ${amount}")
        return True


class ShoppingCart:
    """Shopping cart using strategy pattern."""
    
    def __init__(self, strategy: PaymentStrategy):
        self.items: list = []
        self.strategy = strategy
    
    def add_item(self, item: str, price: float) -> None:
        self.items.append((item, price))
    
    def checkout(self) -> bool:
        total = sum(price for _, price in self.items)
        return self.strategy.pay(total)
```

---

## WEEK 6: ASYNC PROGRAMMING

### Exercise 6.1: Async API Client

Create `src/async_client.py`:
```python
"""Async HTTP client for API interactions."""

import asyncio
import aiohttp
import logging
from typing import List, Dict, Any
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class AsyncAPIClient:
    """Async HTTP client with rate limiting and retry logic."""
    
    def __init__(self, base_url: str, max_concurrent: int = 5):
        self.base_url = base_url
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.session: aiohttp.ClientSession = None
    
    async def __aenter__(self):
        """Context manager entry."""
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        await self.session.close()
    
    async def get(self, endpoint: str) -> Dict[str, Any]:
        """Make async GET request with rate limiting."""
        async with self.semaphore:
            url = f"{self.base_url}{endpoint}"
            try:
                async with self.session.get(url) as response:
                    response.raise_for_status()
                    return await response.json()
            except aiohttp.ClientError as e:
                logger.error(f"API error: {e}")
                raise
    
    async def fetch_multiple(self, endpoints: List[str]) -> List[Dict[str, Any]]:
        """Fetch multiple endpoints concurrently."""
        tasks = [self.get(endpoint) for endpoint in endpoints]
        return await asyncio.gather(*tasks)


# Example usage
async def main():
    """Demonstrate async usage."""
    endpoints = ["/users/1", "/users/2", "/users/3"]
    
    async with AsyncAPIClient("https://jsonplaceholder.typicode.com") as client:
        results = await client.fetch_multiple(endpoints)
        for result in results:
            print(f"User: {result.get('name')}")


if __name__ == "__main__":
    asyncio.run(main())
```

---

## WEEK 7: TESTING

### Exercise 7.1: Comprehensive Tests

Create `tests/test_models.py`:
```python
"""Tests for data models."""

import pytest
from src.models import User, Status, InMemoryRepository, UserFactory


class TestUser:
    """User model tests."""
    
    def test_user_creation(self):
        """Test basic user creation."""
        user = User("Alice", "alice@example.com")
        assert user.name == "Alice"
        assert user.email == "alice@example.com"
        assert user.status == Status.ACTIVE
    
    def test_invalid_email(self):
        """Test email validation."""
        with pytest.raises(ValueError):
            User("Bob", "invalid-email")
    
    def test_user_to_dict(self):
        """Test serialization."""
        user = User("Charlie", "charlie@example.com", tags=["admin"])
        data = user.to_dict()
        assert data["name"] == "Charlie"
        assert "admin" in data["tags"]


class TestRepository:
    """Repository tests."""
    
    def test_save_and_get(self):
        """Test repository operations."""
        repo = InMemoryRepository()
        user = User("David", "david@example.com")
        
        repo.save(user)
        retrieved = repo.get(1)
        
        assert retrieved.name == "David"
    
    def test_get_nonexistent(self):
        """Test retrieving non-existent user."""
        repo = InMemoryRepository()
        assert repo.get(999) is None


class TestUserFactory:
    """Factory tests."""
    
    def test_create_admin(self):
        """Test admin creation."""
        admin = UserFactory.create_admin("Admin", "admin@example.com")
        assert "admin" in admin.tags
    
    def test_create_regular(self):
        """Test regular user creation."""
        user = UserFactory.create_regular("User", "user@example.com")
        assert len(user.tags) == 0
```

Run tests:
```bash
pytest tests/ -v --tb=short
pytest tests/ --cov=src --cov-report=html
```

---

## WEEK 11: API INTEGRATION

### Exercise 11.1: Claude API Integration

Create `src/claude_integration.py`:
```python
"""Integration with Anthropic's Claude API."""

import os
import logging
from typing import Optional
from anthropic import Anthropic

logger = logging.getLogger(__name__)


class ClaudeAssistant:
    """Wrapper around Claude API for specific tasks."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")
        
        self.client = Anthropic(api_key=self.api_key)
        self.conversation_history = []
    
    def code_review(self, code: str) -> str:
        """Review Python code using Claude."""
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": f"""Review the following Python code for:
1. PEP 8 compliance
2. Performance issues
3. Security vulnerabilities
4. Design patterns misuse

Code:
```python
{code}
```

Provide specific, actionable feedback."""
            }]
        )
        return message.content[0].text
    
    def explain_concept(self, concept: str) -> str:
        """Explain a programming concept."""
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"Explain {concept} in Python with a practical example."
            }]
        )
        return message.content[0].text
    
    def chat(self, user_message: str) -> str:
        """Multi-turn conversation."""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system="You are a Python expert assistant helping developers improve their code.",
            messages=self.conversation_history
        )
        
        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message


# Example usage
if __name__ == "__main__":
    assistant = ClaudeAssistant()
    
    # Code review
    bad_code = """
def process_data(data):
    result=[]
    for i in data:
        if i>0:
            result.append(i*2)
    return result
    """
    
    review = assistant.code_review(bad_code)
    print("Code Review:")
    print(review)
```

Install: `pip install anthropic`

---

## CAPSTONE PROJECT STARTER

### Project Template Structure

```
capstone_project/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions
├── src/
│   ├── __init__.py
│   ├── main.py             # Entry point
│   ├── config.py           # Configuration
│   ├── models/             # Data models
│   ├── services/           # Business logic
│   └── api/                # API layer
├── tests/
│   ├── __init__.py
│   ├── unit/
│   ├── integration/
│   └── fixtures/           # Test data
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   └── SETUP.md
├── requirements.txt
├── setup.py
├── pytest.ini
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

### CI/CD Pipeline (.github/workflows/ci.yml)

```yaml
name: Python CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Lint
        run: |
          black --check src/ tests/
          pylint src/
      
      - name: Type check
        run: mypy src/
      
      - name: Run tests
        run: pytest tests/ --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

---

## NEXT STEPS

1. **Week 1**: Commit to setup and environment (Day 1-2)
2. **Week 1**: Complete data types exercises (Day 3-5)
3. **Weeks 2-3**: Master functions and decorators
4. **Weeks 4-5**: Build with OOP and patterns
5. **Weeks 6-8**: Advanced topics (async, testing, optimization)
6. **Weeks 9-11**: Data science & API integration
7. **Weeks 12-16**: Capstone project

**Success Formula:**
- Study: 30%
- Practice: 50%
- Projects: 20%

Start with Week 1 exercises TODAY!
