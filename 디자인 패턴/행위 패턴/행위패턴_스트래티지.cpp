#include <iostream>

using namespace std;

class Attack {
public:
	virtual void attack() = 0;
};

class SwordAttack : public Attack {
public:
	virtual void attack() {
		cout << "Į�� ���� �մϴ�." << endl;
	}
};

class MagicAttack : public Attack {
public:
	virtual void attack() {
		cout << "������ ����մϴ�." << endl;
	}
};

class WhipAttack : public Attack {
public:
	virtual void attack() {
		cout << "���� ��ü�� ä������ ���մϴ�.." << endl;
	}
};

class MonsterAttack : public Attack {
public:
	virtual void attack() {
		cout << "���Ͱ� �̻��� ���� �մϴ�." << endl;
	}
};

class Character {
private:
	Attack* attackMethod;

public:
	virtual void setAttackMethod(Attack* attackMethod) {
		this->attackMethod = attackMethod;
	}

	virtual void attack() {
		attackMethod->attack();
	}
};

class Player : public Character { };
class Monster : public Character { };

int main() {
	Character* player = new Player();
	player->setAttackMethod(new SwordAttack);
	player->attack();

	Character* monster = new Monster();
	monster->setAttackMethod(new MonsterAttack);
	monster->attack();

	player->setAttackMethod(new MagicAttack);
	player->attack();

	cout << "���� óġ �Ϸ�" << endl;

	player->setAttackMethod(new WhipAttack);
	player->attack();

	return 0;
}