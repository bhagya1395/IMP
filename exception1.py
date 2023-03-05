{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ba9b52a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exception handling:\n",
    "there are two types of errors:\n",
    "1)synatx error\n",
    "2)runtime error/logical error/exceptions\n",
    "Q)what is exception:\n",
    ">>some unwanted unexpected event that disturbs normal flow of the program \n",
    "is nothing but exception\n",
    "eg:\n",
    "ZeroDivisionError\n",
    "TypeError\n",
    "ValueError\n",
    "FileNotFoundError\n",
    "EOFError<EndOfError>\n",
    "Q)what is purpose of exception handling\n",
    ">>graceful termination of the program\n",
    "Q)what is meaning of exception handling:\n",
    ">>defining some alternative way to continue rest of the program normally\n",
    "Q)what is default exception handling in python\n",
    ">>terminated program abnormally\n",
    "#python's Exception hierarchy:\n",
    "                          BaseException\n",
    "                               |\n",
    "--------------------------------------------------------------- \n",
    "|               |                 |                           |\n",
    "Exception     SystemExit         GeneratorExit             KeyboardIntrrupt\n",
    "|\n",
    "-------------------------------------------------------------------------------------\n",
    "|                 |              |       |         |            |\n",
    "AttributeError AirthmaticError EOEError NameError lookupError  OSError TypeError ValueError\n",
    "                  |                                |            |\n",
    "                  |-ZeroDivisionError              |-IndexError |-FileNotFoundError\n",
    "                  |-FloatingPointError             |-KeyError   |-InterruptedError\n",
    "                  |-OverflowError                               |-PermissionError\n",
    "                                                                |-TimeOutError\n",
    "                \n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f8ac410f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n"
     ]
    },
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [1]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#Q)what is default exception handling in python\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m10\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhii\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#Q)what is default exception handling in python\n",
    "print(\"hello\")\n",
    "print(10/0)>>riskey code\n",
    "print(\"Hii\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e094b9c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Coustmized Exception Handling:\n",
    "#synatx:\n",
    "try:\n",
    "    Riskey code\n",
    "except:\n",
    "    Handling code\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "69eef4da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "division by zero\n",
      "hii\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello\")\n",
    "try:\n",
    "    print(10/0)\n",
    "except Exception as s:\n",
    "    print(s)\n",
    "    print(\"hii\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "88fbbf01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "stmt-1\n",
      "10.0\n",
      "stmt-3\n"
     ]
    }
   ],
   "source": [
    "print(\"stmt-1\")\n",
    "try:\n",
    "    print(10/0)\n",
    "except ZeroDivisionError:\n",
    "    print(20/2)\n",
    "print(\"stmt-3\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "32d29894",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "this is normal flow of program\n"
     ]
    }
   ],
   "source": [
    "#control flow in try-except block\n",
    "#case-1:If there is no exception:\n",
    "\n",
    "try:\n",
    "    print(\"Hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "except exception as s:#if there is no error in try block,exception block is not executed\n",
    "    print(\"provide proper input to the program\",s)\n",
    "print(\"this is normal flow of program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "0d018777",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "hii\n",
      "this is normal termination\n"
     ]
    }
   ],
   "source": [
    "#case-2:If an exception raised at stmt-2 and corresponding except block match\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(10/0)\n",
    "    print(\"hii\")\n",
    "except Exception:\n",
    "    print(\"hii\")\n",
    "print(\"this is normal termination\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e83a46f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "python\n",
      "this is normal termination\n"
     ]
    }
   ],
   "source": [
    "#case-3:If an exception raised at stmt-2 and but corresponding except block\n",
    "#not matched\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(10/0)\n",
    "    print(\"hiii\")\n",
    "except Exception:\n",
    "    print(\"python\")\n",
    "print(\"this is normal termination\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "be5cf555",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "hiii\n",
      "this is abnormal termination\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"hiii\")\n",
    "except Exception as s:\n",
    "    print(20/0,s)\n",
    "print(\"this is abnormal termination\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "9a2cac69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "exception raised and its discription is: division by zero\n"
     ]
    }
   ],
   "source": [
    "#how to print exception information\n",
    "try:\n",
    "    print(10/0)\n",
    "except ZeroDivisionError as msg:\n",
    "    print(\"exception raised and its discription is:\",msg)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a4e7786b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter first_number:10\n",
      "enter second_number:2.5\n",
      "plez provide int value only\n"
     ]
    }
   ],
   "source": [
    "#try with multiple except blocks:\n",
    "try:\n",
    "    x=int(input(\"enter first_number:\"))\n",
    "    y=int(input(\"enter second_number:\"))\n",
    "    print(x/y)\n",
    "except ZeroDivisionError:\n",
    "    print(\"cannot divide with zero\")\n",
    "except ValueError:\n",
    "    print(\"plez provide int value only\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "c0a2acc1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter first_number:10\n",
      "enter second_number:ten\n",
      "plez provide int value only invalid literal for int() with base 10: 'ten'\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    x=int(input(\"enter first_number:\"))\n",
    "    y=int(input(\"enter second_number:\"))\n",
    "    print(x/y)\n",
    "except ZeroDivisionError as s:\n",
    "    print(\"cannot divide with zero\",s)\n",
    "except ValueError as s:\n",
    "    print(\"plez provide int value only\",s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "ea97c4e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter first_number:10\n",
      "enter second_number:0\n",
      "plez provide valid numbers only and problem is: division by zero\n"
     ]
    }
   ],
   "source": [
    "#single except block that can handle multipe exceptions:\n",
    "try:\n",
    "    x=int(input(\"enter first_number:\"))\n",
    "    y=int(input(\"enter second_number:\"))\n",
    "    print(x/y)\n",
    "except (ZeroDivisionError,ValueError) as msg:\n",
    "    print(\"plez provide valid numbers only and problem is:\",msg)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "ada743c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter first_number:10\n",
      "enter second_number:ten\n",
      "Default Except:plez provide valid input\n"
     ]
    }
   ],
   "source": [
    "#default except block:\n",
    "try:\n",
    "    x=int(input(\"enter first_number:\"))\n",
    "    y=int(input(\"enter second_number:\"))\n",
    "    print(x/y)\n",
    "except ZeroDivisionError :\n",
    "    print(\"ZeroDivisionError: cannot divide with zero\")\n",
    "except:\n",
    "    print(\"Default Except:plez provide valid input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "5ca2e280",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "default 'except:' must be last (908677475.py, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [60]\u001b[1;36m\u001b[0m\n\u001b[1;33m    except:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m default 'except:' must be last\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    x=int(input(\"enter first_number:\"))\n",
    "    y=int(input(\"enter second_number:\"))\n",
    "    print(x/y)\n",
    "except:\n",
    "    print(\"Default Except:plez provide valid input\")\n",
    "except ZeroDivisionError:\n",
    "    print(\"ZeroDivisionError: cannot divide with zero\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82845594",
   "metadata": {},
   "outputs": [],
   "source": [
    "#finally block:purose of finally block is to maintain clenup code\n",
    "#speciality of finally block is whether exception raised or not,\n",
    "handle or not handle finaly block is always executed\n",
    "try: \n",
    "    risky code\n",
    "exception:\n",
    "    handling code\n",
    "finally:\n",
    "    cleanup code\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "5e833de2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "finally\n"
     ]
    }
   ],
   "source": [
    "#case-1:if no exception \n",
    "try:\n",
    "    print(\"try\")\n",
    "except ZeroDivisionError:\n",
    "    print(\"Except\")\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "8397e477",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "Except\n",
      "finally\n"
     ]
    }
   ],
   "source": [
    "#case-2:if an exception raised but handle\n",
    "try:\n",
    "    print(\"try\")\n",
    "    print(10/0)\n",
    "except ZeroDivisionError:\n",
    "    print(\"Except\")\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "f091ed07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "finally\n"
     ]
    },
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [63]\u001b[0m, in \u001b[0;36m<cell line: 2>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m      3\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtry\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 4\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m10\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m:\n\u001b[0;32m      6\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mExcept\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#case-3:if an exception raised but not handle\n",
    "try:\n",
    "    print(\"try\")\n",
    "    print(10/0)\n",
    "except ValueError:\n",
    "    print(\"Except\")\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccca0b19",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "try:\n",
    "    print(\"try\")\n",
    "    os._exit(0)\n",
    "except ZeroDivisionError:\n",
    "    print(\"Except\")\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fdc3245e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
