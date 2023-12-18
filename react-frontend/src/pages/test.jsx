import { useState } from "react"
import {createTest, getAll, getOne} from "../services/test.service"
import { useNavigate } from "react-router-dom";
import { Form, Button, Container, Row, Col } from "react-bootstrap";

export default function Test(){
    const navigate = useNavigate();
    const [test, setTest] = useState({
        strategy: '',
        ticker: '',
        date: ''
    })

    const handleInputChange = (evt) => {
        setTest({...test, [evt.target.name]: evt.target.value})
    }
console.log('before handle submit:',test)
    async function handleSubmit (evt) {
        evt.preventDefault();
        try {
            console.log('what is happening?!')
            const data = {
                strategy: test.strategy,
                ticker: test.ticker,
                date: test.date
            }
            console.log('data is', data)
            const response = await createTest(data);
            console.log('Response is:',response)
            setTest({
                id: response.id,
                strategy: response.strategy,
                date: response.date
            })
            navigate('/result')
        } catch (err) {
            console.log('this isnt working')
            console.log('React Error Message:', err)
        }
    }
    return (
        <Container className="mt-5">
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          <h1 className="text-center text-white">Test A Strategy!</h1>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="strategy">
              <Form.Label>Strategy</Form.Label>
              <Form.Control
                as="select"
                name="strategy"
                value={test.strategy}
                onChange={handleInputChange}
              >
                <option value="5min ORB">5min ORB</option>
                <option value="S/R Break">S/R Break</option>
                <option value="10/20 ema cross">10/20 ema cross</option>
              </Form.Control>
            </Form.Group>
            <Form.Group controlId="ticker">
              <Form.Label>Stock Ticker</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter Stock Ticker"
                name="ticker"
                value={test.ticker}
                onChange={handleInputChange}
              />
            </Form.Group>
            <Form.Group controlId="date" className="mb-3">
              <Form.Label>Date</Form.Label>
              <Form.Control
                type="date"
                name="date"
                value={test.date}
                onChange={handleInputChange}
              />
            </Form.Group>
            <div className="d-grid">
              <Button variant="primary" type="submit" className="w-50 mx-auto">
                Test Strategy
              </Button>
            </div>
          </Form>
        </Col>
      </Row>
      <h1 className="text-center text-white mt-5">RESULTS FROM THE TEST WILL GO DOWN HERE:</h1>
    </Container>
    )
}