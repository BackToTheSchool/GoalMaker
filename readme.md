
# Goal Management Service ����

## 1. ����
### 1.1 ���α׷� �̸�
- Goal Manage
### 1.2. ���α׷� ����
-   ������ �������� ��ǥ�� ����� ������ �� �ְ� ��
    
-   ��ǥ�� �ǽð� �޼����� Ȯ���Ͽ� �޼����� ���̱� ����
    
-   ��ǥ�� �ʹ� ���ų� ������ �������� ���̵��� ������ ������
    
-   ��ǥ�� ���� ����� ���ǹ��� ������� ��� ����
    
-   ��ȭ�н��� ���� �޼����� �н��ϰ� �ൿ�� ��õ��
### 1.3. �ܾ� ����
- �޼��� (Completion Rate)
	- **��ǥ�� ������ Ƚ���� �õ��� Ƚ���� ���� �� (%����)**
-   �ݺ� �ֱ� (Iteration)
	-   �̸� ������ ��ǥ�� �ݺ��ֱ� (��: �ϰ���ǥ, �ְ���ǥ, ������ǥ)
-   �ݺ� ���� (Iteration Unit)
	-   �̸� ������ ��ǥ�� �ݺ� ���� (��: ��, ��, ��)
-   �۾� (Work)
	-   ��ǥ�� Ư���� ��¥�� ���� �۾�
### 1.4. Plan

|��|��|ȭ|��|��|��|��| 
|--|--|--|--|--|--|--|
|  |4/1|4/2|4/3|4/4|4/5|4/6| 
|4/7|4/8|4/9|4/10|4/11|4/12|4/13|
|4/14|4/15|4/16|4/17|4/18|4/19|4/20|
|4/21|4/22|4/23|4/24|4/25|4/26|4/27|
|4/28|4/29|4/30|5/1|5/2|5/3|5/4|
|5/5|5/6|5/7|5/8|5/9|5/10|5/11|
|5/12|5/13|5/14|5/15|5/16|5/17|5/18|
|5/19|5/20|5/21|5/22|5/23|5/24|5/25|
-   1���� (4/1 ~ 4/7)
    

-   ������Ʈ ����
	-   �����ͺ��̽� ����
-   2���� (4/8 ~ 4/14)
	-   ��� ����Ͽ� RESTful API ����
-   3���� (4/15 ~ 4/21)
	-   ������ �����ͺ��̽� ����
	-   �� ����Ʈ ���� �κ� ����
-   4���� (4/22 ~ 4/28)
	-   �ȵ���̵�Http ��Ű� Tensorflow �ȵ���̵忡�� ����ϴ� �� ����
	-   �ȵ���̵� UI ����
-   5���� (4/29 ~ 5/5)
	-   �ȵ���̵� �� ����
	-   �ȵ���̵� ���� ����� �ΰ����� ��� ���� ����(1/2)
-   6���� (5/6 ~ 5/12)
	-   �ȵ���̵� ���� ����� �ΰ����� ��� ���� ����(2/2)
	-   �ӽŷ��װ� �𵨵鿡 ���Ͽ� ����(1/2)
-   7���� (5/13 ~ 5/19)
	-   �ӽŷ��װ� �𵨵鿡 ���Ͽ� ����(2/2)
	-   �ӽŷ��� �� ���� �� �� �н� �ǽ�
-   8���� (5/20 ~ 5/26)
	-   �߰����� ��� ����
	-   QA(��� ����)

### 1.5. ���� ȯ��
-   ���α׷�
	-   Android Studio 3.3.2 for Windows 64-bit
	-   PyCharm 2019 1.1 for Windows 64-bit
	-   PythonAnywhere
	-   sqlite3
	-   Jupyter Notebook
-   ���α׷��� ���
	-   Open Java 1.8
	-   Python 3.7
	-   HTML5
	-   CSS3
	-   JavaScript
-   Ÿ�� ����Ʈ����
	-   Android Marshmallow(6.0)
	-   Website

## 2. �䱸���� (Requirements)
### 2.1. ����� �䱸���� (Functional Requirements)
-   FR 0. �����ͺ��̽� ����
	���α׷��� User, Goal, Work, Prediction 4���� ���̺��� ����մϴ�. �׷��Ƿ� FR�� �����ͺ��̽� ������ ���� �Ʒ��� �� ���� ��ɵ��� �ʿ�� �Ѵ�.
	-   ����(Create)
		- ���̺� �ȿ� �����͸� �����ϴ� ���
	-   �б�(Read)
		- ���̺� ���� �����͸� �д� ���
	-   ����(Update)
		- ���̺� ���� �����͸� �����ϴ� ���
	-   ����(Delete)
		- ���̺� ���� �����͸� �����ϴ� ���. User ���̺��� �Ϻ� ���̺��� �����ʹ� �����ϴµ� ���� �� ���� �ִ�.

-   FR 1. ��ǥ ����
	�� ����ڵ鿡 ���� ��ǥ�� ����, ����, ���� �׸��� �޼����� �����ϴ� ����̴�. ��� ����ڵ��� ������ ���� �ൿ���� �� �� �ִ�.
	-   ��Ȳ 1. ��ǥ ����
		�� ��Ȳ������, Goal ���̺��� ��� �ȴ�. ����ڵ��� ������ ���� �����͵��� �Է��ؾ� �Ѵ�.
		-   ��ǥ �̸�(Goal Title)    
		-   ��ǥ �ݺ� �ֱ�(Goal Iteration)
    -   ��Ȳ 2. ��ǥ ����
	    �� ��Ȳ������ ��ǥ �ݺ� �ֱ⿡ ���� �ڵ������� ��ǥ�� �����ȴ�. �׸��� ����ڵ��� �ݵ�� �޼����� �����ؾ� �Ѵ�.

	-  ��Ȳ 3. ��ǥ ����
		�� ��Ȳ������ ����ڴ� �����̸Ӹ� Ű�� ������ ��ǥ�� ��Ʈ����Ʈ�� ������ �� �ִ�.
	-   ��Ȳ 4. ��ǥ ����
	    �� ��Ȳ���� ����ڴ� Ư�� ��ǥ�� ���� �� �� �ִ�.
-   FR 2. ��ǥ ���
	�� FR�� ��ǥ���� ���� ���ġ�� ���� �׷��� ���·� �����ش�. �� ���񽺿����� �� ���� ��� ���� �׷��� ���·� �����Ѵ�.
	-   ���� ������
	    ��ǥ���� ������ �� ���� ���·� ��������.
		-   ���� ������
		    ���� �����ʹ� ��ǥ�� �޼����� �ݺ� ������ �������� �����ش�.
		-   ���� ������
			���� �����ʹ� Ư�� �Ⱓ�� ���� ��ǥ�� �޼����� Ư�� �Ⱓ�� ��ü ��ǥ�� �޼����� �ΰ��� ���·� ���� �ȴ�.
	-   ���� ���
		���� ��ǥ���� �޼����� ������� ���� �ݺ� �Ⱓ�� �޼����� ������ ����� �����Ѵ�.

-   FR 3. �޼��� ����
	�� FR�� ���� �ݺ� �Ⱓ�� �޼����� �����ϴ� ����̴�. �޼����� �������̹Ƿ�, �ӽŷ��� �˰����� ȸ�ͺм��� ����Ѵ�. ������ �˰��� �ĺ����̴�.
	-   ���� ȸ�� �м� (Linear Regression)
	-   Lasso ȸ�� �м� (Lasso Regression)
	-   �ɼ� ȸ�� �м� (Ridge Regression)
	-   ������ƽ ȸ�� �м� (Logistic Regression)
	-   K-�ִ� �̿� ȸ�� �м� (K nearest neighbor Regression)

	������ ��Ȯ���� ���̱� ���� ���� �ӻ�� �н��� �� �ϳ��� �� ���̴�.
	-   Bagging Regressor
	-   Pasting
	-   Bagging
	-   Ada Boost
	-   Gradient Boosting

### 2.2. ������ �䱸����(Non-Functional Requirements)
-   NFR 1. ���̺� ����
    ���� ����ڵ��� ���񽺿� �α��� �Ͽ��� ���, ��ǥ �����Ͽ� ���� ������ ó���ϴµ� ���� �ð��� �ʿ��� ���̴�. �׷��Ƿ� ���񽺴� �� ������ �ذ��ϱ� ���� ���� ĳ�ø� ����� ���̴�. ����ڰ� ��⿡ �α������� ���, ����ڿ� ���õ� ��ü �����͸� ��⿡ �ڵ����� �ٿ�ε� �Ѵ�. �׸��� ����ڰ� ��ǥ �߰�, ����, ������ ���� �ൿ�� �Ѵٸ�, �����ʹ� ���� ������ ���� �� ���̴�. �׸��� ����ڰ� �α׾ƿ� �ϸ� ��ü �����ʹ� ���ÿ��� ���� �Ѵ�.

## 3. ����
### 3.1. Use-case Diagram
#### ![Figure 1. Use-case Diagram Image](./md_images/Figure1_Use_Case_Diagram.JPG)

### 3.2. Class Diagram

#### ![Figure 2. Class Diagram Image](./md_images/Figure2_Class_Diagram.JPG) 

- Goal Class
	- Attribute
		-  Iteration : enum, �ݺ� �ֱ��� ����; DAILY, WEEKLY, MONTHLY
		-   name : String, ��ǥ�� �̸�
		-   iterationType : Iteration, �ݺ� ����
		-   frequency : int, �� ��ǥ�� �Ⱓ���� ��ǥ �ݺ� Ƚ��(ex. �� 1ȸ, �� 3ȸ)
		-   dailyFreq : int[], �ϰ� ��ǥ�� ���� ��ǥ �ݺ� Ƚ��
		-   objectTime : int, ��ǥ�� �޼�ġ
		-   completeDay : int, ��ǥ�� ���� Ƚ��
		-   startDay : Date, ��ǥ�� ���� ��¥
	-   Operation
		-   Goal(String name, int frequency, int objectTime, int completeDay, Date startDay, Iteration iterationType) : void, �ְ� ��ǥ�� ���� ��ǥ�� ������
		-   Goal(String name, int[] frequency, int objectTime, int completeDay, Date startDay) : void, �ϰ� ��ǥ�� ������
		-   getCompletionRate(int comp) : int, �ش� ��ǥ�� ��ü �޼����� ������
		-   createGoal(String name, Iteration iteration , int frequency, int objTime) : void, ��ǥ�� ����� ���� DB�� ������
		-   updateGoal(String name, Iteration iteration, int frequency, int objTime): void, ��ǥ�� �����ϰ� �� ���� ���� DB�� ������
		-   deleteGoal(String name) : void, ���� DB���� �ش� ��ǥ�� ������
		-   downloadData() : void, ���� DB���� ��ü �����͸� ����DB�� �ٿ�ε���
		-   uploadData() : void, ���� DB�� ��ü �����͸� ���� DB�� ���ε���
		-   getLocalItemList() : ArrayList<Goal>, ���� DB�� ��ǥ ����Ʈ�� ������
		-   isAvailable() : boolean, �����ͺ��̽��� ��ǥ�� �߰��� �� �ִ��� ������ Ȯ����(���Ἲ �������� Ȯ��)
		-   isDataSynched() : Boolean, ����DB�� ����DB�� �����Ͱ� ����ȭ �Ǿ����� Ȯ��
-  Work Class
	-   Attribute
		-   name : String, �۾��� �̸�
		-   objectTime : int, �۾��� ��ǥġ(��ǥ�� objectTime�� ����)
		-   completeTime : int, �ش� ��¥�� �۾��� ���� ���� Ƚ��.
		-   date : Date, �۾��� ��¥
	-   Operation
		-   Work(String name, int objectTIme) : void, ������. completeTime = 0, date = Today()�� �⺻������ �ʱ�ȭ �ȴ�.
		-   getCompletionRate(int obj, int comp) : int, �ش� ��¥�� �޼����� �����Ѵ�
		-   createWork(String name, int objectTime, int completeTime, Date date) : void, �۾��� �����ϰ� ����DB�� �߰��Ѵ�.
		-   updateWork(String name, int objectTime, int completionTime, Data date): void, �۾��� �����ϰ� ���� DB�� �����Ѵ�.
		-   deleteWork(String name, Date date) : void, ����DB���� �۾��� �����Ѵ�
		-   downloadData() : void, ���� DB�� �����͸� ����DB�� �ٿ�ε��Ѵ�.
		-   uploadData() : void, ����DB�� �����͸� ����DB�� ���ε��Ѵ�.
		-   getLocalItemList() : ArrayList<Work>, �۾��� ����DB�� ����� ����Ѵ�.
		-   isDataSynched() : boolean, �۾��� ���� DB���� ���� DB���� ����ȭ �Ǿ����� Ȯ���Ѵ�.
- User Class
	-   Attribute
		-   userId : String, ������� ID, �����̸Ӹ� Ű
		-   password : String, ������� ��й�ȣ
		-   name : String, ������� �̸�

### 3.3. Relational DB Diagram
#### ![Figure 3. Relational DB Diagram Image](./md_images/Figure3_Relational_DB_Diagram.JPG)