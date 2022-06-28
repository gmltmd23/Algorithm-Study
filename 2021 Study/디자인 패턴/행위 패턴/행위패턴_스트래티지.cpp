#include <iostream>

using namespace std;

class Attack {
public:
	virtual void attack() = 0;
};

class SwordAttack : public Attack {
public:
	virtual void attack() {
		cout << "칼로 공격 합니다." << endl;
	}
};

class MagicAttack : public Attack {
public:
	virtual void attack() {
		cout << "마법을 사용합니다." << endl;
	}
};

class WhipAttack : public Attack {
public:
	virtual void attack() {
		cout << "몬스터 사체에 채찍질을 가합니다.." << endl;
	}
};

class MonsterAttack : public Attack {
public:
	virtual void attack() {
		cout << "몬스터가 이빨로 공격 합니다." << endl;
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

	cout << "몬스터 처치 완료" << endl;

	player->setAttackMethod(new WhipAttack);
	player->attack();

	return 0;
}