from sqlalchemy import (
    Column,
    Integer,
    Date,
    BigInteger,
    CHAR,
    NVARCHAR,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from main import engine

Base = declarative_base()


class loan_remittance(Base):

    __tablename__ = "loan_remittance"

    loan_remittance_id = Column(
        BigInteger, primary_key=True, autoincrement=True
    )
    loan_id = Column(BigInteger, ForeignKey("loan.loan_id"), nullable=False)
    as_of_date = Column(Date, nullable=False)
    servicer_id = Column(Integer, nullable=False)

    loan = relationship("loan", back_populates="loan_remittance")


class loan(Base):

    __tablename__ = "loan"

    loan_id = Column(BigInteger, primary_key=True)
    eresi_id = Column(CHAR(50), nullable=False)
    seller_loan_number = Column(NVARCHAR(50), nullable=False)

    loan_remittance = relationship("loan_remittance", back_populates="loan")

Base.metadata.create_all(engine)    
