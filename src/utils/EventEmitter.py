from enum import Enum
from functools import wraps
from typing import Any, Callable, Dict, Generic, List, Type, TypeVar

TEventTypeEnum = TypeVar('TEventTypeEnum', bound=Enum)

# Custom type hint representing a function that takes an argument of type TEventTypeEnum
# followed by any number of additional arguments
# EventHandler = Callable[[TEventTypeEnum, *Any], Any]
EventHandler = Callable[[TEventTypeEnum], Any]


class EventEmitter(Generic[TEventTypeEnum]):
    def __init__(self, event_enum: Type[TEventTypeEnum]) -> None:
        self._event_handlers: Dict[TEventTypeEnum, List[EventHandler]] = {}
        self._event_enum: type[TEventTypeEnum] = event_enum

    def add_event_subscription(self, event_type: TEventTypeEnum, handler: EventHandler) -> None:
        """Add an event handler for the specified event."""
        if event_type not in self._event_handlers:
            self._event_handlers[event_type] = []
        self._event_handlers[event_type].append(handler)

    def remove_event_subscription(self, event_type: TEventTypeEnum, handler: EventHandler) -> None:
        """Remove an event handler for the specified event."""
        if event_type in self._event_handlers:
            self._event_handlers[event_type].remove(handler)

    def emit_event(self, event_type: TEventTypeEnum, *args: Any, **kwargs: Any) -> None:
        """Emit the specified event, calling all registered event handlers."""
        if event_type in self._event_handlers:
            for handler in self._event_handlers[event_type]:
                handler(event_type, *args, **kwargs)

    @staticmethod
    def emits(event_type: TEventTypeEnum, *event_args: Any, **event_kwargs: Any):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                # Assuming the event emitter instance is the first argument
                event_emitter: EventEmitter = args[0]
                event_emitter.emit_event(
                    event_type, *event_args, **event_kwargs)
                return result
            return wrapper
        return decorator
