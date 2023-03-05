{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7748aa8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "exception is division by zero\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(2/0)\n",
    "except ZeroDivisionError as s:\n",
    "    print(\"exception is\",s)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d4f40179",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "exception is division by zero\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(2/0)\n",
    "except Exception as s:\n",
    "    print(\"exception is\",s)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e5b5f8e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i am here\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(2/0)\n",
    "except Exception as d:\n",
    "    print(\"i am here\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f958ec77",
   "metadata": {},
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [14]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m2\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "print(2/0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f5b9423",
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    statement1\n",
    "    statement2\n",
    "    \n",
    "except:\n",
    "    statement1\n",
    "    statement2\n",
    "else:\n",
    "finally:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "bdf6e706",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "exception is unsupported operand type(s) for /: 'int' and 'str'\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(10/\"ten\")\n",
    "except Exception as s:\n",
    "    print(\"exception is\",s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "51e03173",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "12.4\n",
      "plez provide the integer numbers only invalid literal for int() with base 10: '12.4'\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    x=int(input())\n",
    "    y=int(input())\n",
    "    z=x+y\n",
    "except Exception as s:\n",
    "    print(\"plez provide the integer numbers only\",s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "b0c173e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "exception is division by zero\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(2/0)\n",
    "    print(10/\"ten\")\n",
    "except Exception as s:\n",
    "    print(\"exception is\",s)\n",
    "except exception as d:\n",
    "    print(\"exception is\",d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a21b0235",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "\"iam kanchan\"\n",
      "enter proper input invalid literal for int() with base 10: '\"iam kanchan\"'\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    x=int(input())\n",
    "    y=int(input())\n",
    "    z=x+y\n",
    "except(ValueError,KeyError,ZeroDivisionError) as s:\n",
    "    print(\"enter proper input\",s)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "c6961454",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iam kanchan\n",
      "plez provide proper input\n",
      "fially\n"
     ]
    }
   ],
   "source": [
    "#Neasted exception\n",
    "try:\n",
    "    print(\"iam kanchan\")\n",
    "    #print(10/0)\n",
    "    try:\n",
    "        print(2/0)\n",
    "    except Exception as m:\n",
    "        print(\"plez provide proper input\")\n",
    "except (ValueError,NameError,ZeroDivisionError) as s:\n",
    "    print(\"Exception is\",s )\n",
    "finally:\n",
    "    print(\"fially\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "5281ba4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iam kanchan\n",
      "enter proper input division by zero\n",
      "iam finally\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(\"iam kanchan\")\n",
    "    print(10/0)\n",
    "except(ValueError,KeyError,ZeroDivisionError) as s:\n",
    "    print(\"enter proper input\",s)\n",
    "finally:\n",
    "    print(\"iam finally\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "fa418d66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iam kanchan\n",
      "plez provide proper input division by zero\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(\"iam kanchan\")\n",
    "    #print(10/0)\n",
    "finally:\n",
    "    try:\n",
    "        print(2/0)\n",
    "    except Exception as m:\n",
    "        print(\"plez provide proper input\",m)\n",
    "    #finally:\n",
    "        #print(\"iam  inside inner block\")\n",
    "#except (ValueError,NameError,ZeroDivisionError) as s:\n",
    "   # print(\"Exception is\",s )\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "fbc2d0bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iam kanchan\n",
      "hello division by zero\n",
      "iam finally\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(\"iam kanchan\")\n",
    "    #print(10/0)\n",
    "except Exception as e:\n",
    "    print(\"Exception\",e)\n",
    "else:\n",
    "    try:\n",
    "        print(23/0)\n",
    "    except Exception as s:\n",
    "        print(\"hello\",s)\n",
    "finally:\n",
    "    print(\"iam finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23c406e6",
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
